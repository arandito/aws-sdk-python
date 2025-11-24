# docs/scripts/generate_nav.py
"""
Generate client documentation navigation dynamically.

Executed by mkdocs-gen-files during the build process after generate_doc_stubs.py.
It discovers client documentation already generated in docs/clients/ by generate_doc_stubs.py
and generates a dynamic index (clients/index.md) that groups clients alphabetically.
"""

import logging
import sys

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import mkdocs_gen_files


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("generate_nav")


@dataclass
class ClientDocInfo:
    """Information about a client's documentation directory."""

    name: str
    package_name: str
    docs_path: Path


def generate_nav(repo_root: Path) -> int:
    """Generate navigation for clients."""
    try:
        clients = discover_clients(repo_root)
        generate_clients_index(clients)
        build_nav_structure(clients)
    except Exception as e:
        logger.error(f"Error generating navigation: {e}")
        return 1

    return 0


def discover_clients(repo_root: Path) -> list[ClientDocInfo]:
    """Discover clients from clients packages."""
    clients = []
    clients_dir = repo_root / "clients"

    if not clients_dir.exists():
        raise FileNotFoundError(f"No clients directory found at {clients_dir}")

    for client_path in sorted(clients_dir.iterdir()):
        if not client_path.is_dir() or client_path.name == "aws-sdk-python":
            continue

        # Extract service name from package name (e.g., "aws-sdk-bedrock-runtime" -> "Bedrock Runtime")
        service_name = client_path.name.replace("aws-sdk-", "").replace("-", " ").title()
        package_name = client_path.name

        clients.append(ClientDocInfo(
            name=service_name,
            package_name=package_name,
            docs_path=client_path,
        ))

        logger.info(f"✅ Discovered client: {service_name}")

    return clients


def generate_clients_index(clients: list[ClientDocInfo]) -> None:
    """Generate clients/index.md (with alphabetical tabs)."""
    content = "# All Available Clients\n\n"

    # Group by first letter
    grouped = defaultdict(list)
    for client in clients:
        letter = client.name[0].upper()
        grouped[letter].append(client)

    # Tab for all services
    content += "=== \"All\"\n\n"
    content += "    | Service | Package Name |\n"
    content += "    |----------|--------------|\n"
    for client in sorted(clients, key=lambda x: x.name):
        content += f"    | **[{client.name}]({client.name}/index.md)** | `{client.package_name}` |\n"
    content += "\n"

    # Individual letter tabs
    for letter in sorted(grouped.keys()):
        content += f"=== \"{letter}\"\n\n"
        content += "    | Service | Package Name |\n"
        content += "    |----------|--------------|\n"
        for client in sorted(grouped[letter], key=lambda x: x.name):
            content += f"    | **[{client.name}]({client.name}/index.md)** | `{client.package_name}` |\n"
        content += "\n"

    with mkdocs_gen_files.open("clients/index.md", "w") as f:
        f.write(content)

    logger.info(f"✅ Generated clients index page with {len(clients)} letter tabs")


def build_nav_structure(clients: list[ClientDocInfo]) -> None:
    """Build navigation structure for clients."""
    nav_structure = [
        {
            "Getting Started": [
                {"Overview": "index.md"},
                {"Contributing": "contributing/index.md"},
            ]
        },
        {
            "Clients API Reference": [
                "clients/index.md",
                *[f"clients/{client.name}/index.md" for client in sorted(clients, key=lambda x: x.name)]
            ]
        }
    ]
    mkdocs_gen_files.config["nav"] = nav_structure
    logger.info(f"✅ Generated navigation structure for {len(clients)} clients")


def main() -> int:
    """Main entry point to generate navigation."""
    repo_root = Path(__file__).parent.parent

    return generate_nav(repo_root)


if __name__ == "__main__":
    sys.exit(main())
else:
    # When imported by mkdocs-gen-files, run the generation
    main()