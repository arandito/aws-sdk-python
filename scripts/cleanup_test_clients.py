#!/usr/bin/env python3
"""
Clean up test client copies created by create_test_clients.py.
Removes all aws-sdk-bedrock-runtime-N directories.

Usage:
  ./cleanup_test_clients.py                    # Remove all test clients in batches of 100
  ./cleanup_test_clients.py --all              # Remove all test clients at once
  ./cleanup_test_clients.py --start 1 --end 100   # Remove only clients 1-100
  ./cleanup_test_clients.py --batch-size 50    # Remove all in batches of 50
"""

import argparse
import shutil
import re
from pathlib import Path


def get_client_number(name: str) -> int | None:
    """Extract the client number from a directory name."""
    match = re.match(r'^aws-sdk-bedrock-runtime-(\d+)$', name)
    return int(match.group(1)) if match else None


def cleanup_clients(start: int | None, end: int | None, clients_dir: Path):
    """
    Remove test clients. If start/end are None, removes all test clients.
    Otherwise, removes only clients in the specified range.
    """
    # Pattern to match test clients: aws-sdk-bedrock-runtime-<number>
    pattern = re.compile(r'^aws-sdk-bedrock-runtime-\d+$')

    removed_count = 0

    for item in clients_dir.iterdir():
        if not (item.is_dir() and pattern.match(item.name)):
            continue

        # Check if this client is in the requested range
        if start is not None or end is not None:
            client_num = get_client_number(item.name)
            if client_num is None:
                continue
            if start is not None and client_num < start:
                continue
            if end is not None and client_num > end:
                continue

        print(f"Removing {item.name}...")
        shutil.rmtree(item)
        removed_count += 1

        if (removed_count % 25) == 0:
            print(f"  Progress: {removed_count} clients removed in this batch")

    return removed_count


def main():
    parser = argparse.ArgumentParser(
        description="Clean up test client copies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--start",
        type=int,
        help="Start index (removes only clients >= this number)"
    )
    parser.add_argument(
        "--end",
        type=int,
        help="End index (removes only clients <= this number)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size when removing all clients (default: 100)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Remove all test clients at once without batching"
    )

    args = parser.parse_args()

    # Get the repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent
    clients_dir = repo_root / "clients"

    if not clients_dir.exists():
        print(f"Error: Clients directory not found at {clients_dir}")
        return

    # Determine the operation mode
    if args.start is not None or args.end is not None:
        # Specific range requested
        start = args.start
        end = args.end
        range_desc = f"{start or 'beginning'}-{end or 'end'}"
        print(f"Removing test clients in range {range_desc}...")
        removed = cleanup_clients(start, end, clients_dir)
        print(f"\nDone! Removed {removed} test clients.")

    elif args.all:
        # Remove all at once
        print("Removing all test clients at once...")
        removed = cleanup_clients(None, None, clients_dir)
        print(f"\nDone! Removed {removed} test clients.")

    else:
        # Remove in batches (default)
        batch_size = args.batch_size
        total_removed = 0

        print(f"Removing test clients in batches of {batch_size}...")

        for batch_start in range(1, 399, batch_size):
            batch_end = min(batch_start + batch_size - 1, 398)
            print(f"\n--- Batch: clients {batch_start}-{batch_end} ---")
            removed = cleanup_clients(batch_start, batch_end, clients_dir)
            total_removed += removed
            print(f"Batch complete: {removed} removed")

            if removed == 0:
                # No more clients to remove
                break

        print(f"\nAll done! Removed {total_removed} test clients.")


if __name__ == "__main__":
    main()
