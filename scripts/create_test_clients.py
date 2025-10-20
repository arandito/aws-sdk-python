#!/usr/bin/env python3
"""
Create 398 test client copies to simulate a large number of clients.
This helps benchmark documentation generation time.

Usage:
  ./create_test_clients.py              # Create all 398 clients in batches of 100
  ./create_test_clients.py --all        # Create all 398 clients at once
  ./create_test_clients.py --start 1 --end 100    # Create clients 1-100
  ./create_test_clients.py --batch-size 50        # Create all in batches of 50
"""

import argparse
import shutil
import re
from pathlib import Path


def create_clients(start: int, end: int, clients_dir: Path, source_client: Path):
    """Create test clients from start to end (inclusive)."""
    created_count = 0
    skipped_count = 0

    for i in range(start, end + 1):
        target_name = f"aws-sdk-bedrock-runtime-{i}"
        target_dir = clients_dir / target_name

        if target_dir.exists():
            print(f"Skipping {target_name} (already exists)")
            skipped_count += 1
            continue

        # Copy the entire directory
        print(f"Creating {target_name}...")
        shutil.copytree(source_client, target_dir)

        # Update pyproject.toml to avoid name conflicts
        pyproject_path = target_dir / "pyproject.toml"
        if pyproject_path.exists():
            content = pyproject_path.read_text()

            # Update package name
            content = re.sub(
                r'name = "aws-sdk-bedrock-runtime"',
                f'name = "aws-sdk-bedrock-runtime-{i}"',
                content
            )

            # Update site_name for docs
            content = re.sub(
                r'site_name = "([^"]*)"',
                rf'site_name = "\1 {i}"',
                content
            )

            pyproject_path.write_text(content)

        created_count += 1

        if (created_count % 25) == 0:
            print(f"  Progress: {created_count} clients created in this batch")

    return created_count, skipped_count


def main():
    parser = argparse.ArgumentParser(
        description="Create test client copies for benchmarking",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--start",
        type=int,
        help="Start index (default: 1)"
    )
    parser.add_argument(
        "--end",
        type=int,
        help="End index (default: 398)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size when creating all clients (default: 100)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Create all clients at once without batching"
    )

    args = parser.parse_args()

    # Get the repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent
    clients_dir = repo_root / "clients"
    source_client = clients_dir / "aws-sdk-bedrock-runtime"

    if not source_client.exists():
        print(f"Error: Source client not found at {source_client}")
        return

    # Determine the range
    if args.start is not None or args.end is not None:
        # Specific range requested
        start = args.start if args.start is not None else 1
        end = args.end if args.end is not None else 398
        print(f"Creating test clients {start}-{end}...")
        created, skipped = create_clients(start, end, clients_dir, source_client)
        print(f"\nDone! Created {created} clients, skipped {skipped}.")

    elif args.all:
        # Create all at once
        print("Creating all 398 test clients at once...")
        created, skipped = create_clients(1, 398, clients_dir, source_client)
        print(f"\nDone! Created {created} clients, skipped {skipped}.")

    else:
        # Create in batches (default)
        batch_size = args.batch_size
        total_created = 0
        total_skipped = 0

        print(f"Creating 398 test clients in batches of {batch_size}...")

        for batch_start in range(1, 399, batch_size):
            batch_end = min(batch_start + batch_size - 1, 398)
            print(f"\n--- Batch: clients {batch_start}-{batch_end} ---")
            created, skipped = create_clients(batch_start, batch_end, clients_dir, source_client)
            total_created += created
            total_skipped += skipped
            print(f"Batch complete: {created} created, {skipped} skipped")

        print(f"\nAll done! Created {total_created} clients, skipped {total_skipped}.")
        print(f"Total clients in directory: {2 + total_created} (2 original + {total_created} copies)")


if __name__ == "__main__":
    main()
