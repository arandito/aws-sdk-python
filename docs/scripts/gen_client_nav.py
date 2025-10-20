# docs/scripts/gen_client_nav.py
"""
Generate client documentation structure dynamically.

Executed by mkdocs-gen-files during the build process.
It discovers all client packages, copies their docs into the virtual
docs tree, and generates a dynamic index (clients/index.md) that groups
clients alphabetically.
"""

from pathlib import Path
import mkdocs_gen_files
from collections import defaultdict

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
docs_root = Path(__file__).parent.parent
repo_root = docs_root.parent
clients_dir = repo_root / "clients"

# -----------------------------------------------------------------------------
# Discover clients
# -----------------------------------------------------------------------------
clients = []

if clients_dir.exists():
    for client_path in sorted(clients_dir.iterdir()):
        if not client_path.is_dir():
            continue

        # Skip meta package
        if client_path.name == "aws-sdk-python":
            continue

        client_docs = client_path / "docs"
        if not client_docs.exists():
            continue

        display_name = (
            client_path.name
            .replace("aws-sdk-", "")
            .replace("-", " ")
            .title()
        )

        clients.append({
            "name": display_name,
            "package": client_path.name,
            "path": client_path,
            "docs": client_docs,
        })

        print(f"✓ Discovered client: {display_name}")

if not clients:
    print("⚠️  No clients found under", clients_dir)

# -----------------------------------------------------------------------------
# Copy all client docs into the virtual docs structure
# -----------------------------------------------------------------------------
for client in clients:
    client_docs = client["docs"]
    package_name = client["package"]

    for doc_file in client_docs.rglob("*.md"):
        rel_path = doc_file.relative_to(client_docs)
        virtual_path = Path("clients") / package_name / rel_path

        with mkdocs_gen_files.open(virtual_path, "w") as f:
            f.write(doc_file.read_text())

        mkdocs_gen_files.set_edit_path(
            virtual_path,
            Path("..") / client_docs.relative_to(repo_root) / rel_path
        )

# -----------------------------------------------------------------------------
# Generate clients/index.md (with alphabetical tabs)
# -----------------------------------------------------------------------------
with mkdocs_gen_files.open("clients/index.md", "w") as f:
    f.write("# All AWS Service Clients\n\n")
    f.write(f"Currently, the AWS SDK for Python provides clients for **{len(clients)} services**.\n\n")

    # Group by first letter
    grouped = defaultdict(list)
    for c in clients:
        letter = c["name"][0].upper()
        if not letter.isalpha():
            letter = "#"
        grouped[letter].append(c)

    # All tab
    f.write("=== \"All\"\n\n")
    f.write("    | Service | Package Name |\n")
    f.write("    |----------|--------------|\n")
    for c in sorted(clients, key=lambda x: x["name"]):
        f.write(f"    | **[{c['name']}]({c['package']}/index.md)** | `{c['package']}` |\n")
    f.write("\n")

    # Letter tabs
    for letter in sorted(grouped.keys()):
        f.write(f"=== \"{letter}\"\n\n")
        f.write("    | Service | Package Name |\n")
        f.write("    |----------|--------------|\n")
        for c in sorted(grouped[letter], key=lambda x: x["name"]):
            f.write(f"    | **[{c['name']}]({c['package']}/index.md)** | `{c['package']}` |\n")
        f.write("\n")

print(f"✓ Generated clients index page with {len(clients)} letter tabs")

# -----------------------------------------------------------------------------
# Generate SUMMARY.md navigation
# -----------------------------------------------------------------------------
clients_nav = [
    f"    * [{c['name']}]({Path('clients') / c['package'] / 'index.md'})"
    for c in clients
]

summary_template = (docs_root / "SUMMARY.md").read_text()
summary_with_clients = summary_template.replace(
    "    {{clients_nav.md}}",
    "\n".join(clients_nav)
)

with mkdocs_gen_files.open("SUMMARY.md", "w") as f:
    f.write(summary_with_clients)

print(f"✓ Injected {len(clients_nav)} clients into SUMMARY.md")
print(f"✅ Finished generating documentation for {len(clients)} clients.")
