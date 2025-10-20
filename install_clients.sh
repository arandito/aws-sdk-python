#!/bin/bash

# Script to install all client packages in editable mode using uv
# Excludes the aws-sdk-python meta-package

set -e  # Exit on error

CLIENTS_DIR="clients"
EXCLUDED="aws-sdk-python"
INSTALLED_COUNT=0
FAILED_COUNT=0
FAILED_PACKAGES=()

echo "Starting installation of client packages..."
echo "Excluding: $EXCLUDED"
echo ""

# Loop through all directories in the clients folder
for client_dir in "$CLIENTS_DIR"/*/ ; do
    # Get the directory name without the trailing slash
    client_name=$(basename "$client_dir")

    # Skip the excluded package
    if [ "$client_name" = "$EXCLUDED" ]; then
        echo "Skipping $client_name (excluded)"
        continue
    fi

    # Check if pyproject.toml exists (to verify it's a valid package)
    if [ -f "$client_dir/pyproject.toml" ]; then
        echo "Installing: $client_name"
        if uv pip install -e "$client_dir"; then
            ((INSTALLED_COUNT++))
        else
            echo "  ❌ Failed to install $client_name"
            ((FAILED_COUNT++))
            FAILED_PACKAGES+=("$client_name")
        fi
    else
        echo "Skipping $client_name (no pyproject.toml found)"
    fi
done

echo ""
echo "================================"
echo "Installation Summary"
echo "================================"
echo "Successfully installed: $INSTALLED_COUNT packages"
echo "Failed: $FAILED_COUNT packages"

if [ $FAILED_COUNT -gt 0 ]; then
    echo ""
    echo "Failed packages:"
    for pkg in "${FAILED_PACKAGES[@]}"; do
        echo "  - $pkg"
    done
    exit 1
fi

echo ""
echo "All client packages installed successfully!"
