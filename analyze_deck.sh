#!/bin/bash
# Helper script for Claude to analyze deck power levels
# Usage: ./analyze_deck.sh <deck_file>

if [ $# -eq 0 ]; then
    echo "Usage: ./analyze_deck.sh <deck_file>"
    echo ""
    echo "Available decks:"
    ls -1 options/*.md | xargs -n1 basename
    exit 1
fi

DECK_FILE="$1"

# Generate the URL
python3 generate_deck_url.py "$DECK_FILE"
