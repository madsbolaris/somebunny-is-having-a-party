#!/bin/bash
# Generate EDH Power Level URLs for all deck files in the options/ folder

echo "Generating EDH Power Level URLs for all deck files..."
echo ""

for deck_file in options/*.md; do
    deck_name=$(basename "$deck_file" .md)
    echo "=== $deck_name ==="
    python3 generate_deck_url.py "$deck_file"
    echo ""
done
