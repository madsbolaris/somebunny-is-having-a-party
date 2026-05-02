#!/usr/bin/env python3
"""
Analyze EDH deck power levels using edhpowerlevel.com
Returns analysis results for Claude to use.
Requires playwright: pip install playwright && playwright install chromium
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import quote_plus


def parse_deck_file(filepath):
    """Parse deck list file and return list of card entries."""
    cards = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                cards.append('')
                continue

            parts = line.split(None, 1)
            if len(parts) == 2:
                quantity, card_name = parts
                card_entry = f"{quantity} {card_name}"
                cards.append(card_entry)

    return cards


def generate_url(cards):
    """Generate EDH Power Level URL from card entries."""
    url_parts = []
    for card in cards:
        if card == '':
            url_parts.append('')
        else:
            # URL encode the card name (spaces become +, commas become %2C, etc)
            encoded = quote_plus(card)
            url_parts.append(encoded)

    deck_string = '~'.join(url_parts)
    deck_string += '~Z~'

    return f"https://edhpowerlevel.com/?d={deck_string}"


def fetch_with_playwright(url):
    """Fetch page content using Playwright to render JavaScript."""
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until='domcontentloaded', timeout=15000)

            # Wait for JavaScript calculations to complete
            page.wait_for_timeout(4000)

            # Get text content instead of HTML
            text = page.inner_text('body')
            browser.close()
            return text

    except ImportError:
        print("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to fetch page: {e}", file=sys.stderr)
        sys.exit(1)


def parse_results(text):
    """Extract power level metrics from rendered page text."""
    results = {}

    # Patterns that handle line breaks between labels and values
    patterns = {
        'power_level': [
            r'Power Level[\s\n]+([\d.]+)[\s\n]+/[\s\n]+10',
        ],
        'efficiency': [
            r'Efficiency[\s\n]+([\d.]+)[\s\n]+/[\s\n]+10',
        ],
        'impact': [
            r'Total Impact[\s\n]+([\d.]+)',
            r'Impact[\s\n]+([\d.]+)',
        ],
        'score': [
            r'Score[\s\n]+([\d]+)[\s\n]+/[\s\n]+1000',
        ],
        'tipping_point': [
            r'Tipping Point[\s\n]+([\d]+)',
        ],
        'avg_playability': [
            r'Average Playability[\s\n]+([\d.]+)%',
        ],
        'commander_bracket': [
            r'Commander Bracket:\s+(\d+)',
        ],
        'mana_screw': [
            r'Mana Screw[\s\n]+([\d.]+)%\s+Chance',
        ],
        'mana_flood': [
            r'Mana Flood[\s\n]+([\d.]+)%\s+Chance',
        ],
        'mana_optimal': [
            r'Sweet Spot[\s\n]+([\d.]+)%\s+Chance',
        ],
        'lands': [
            r'(\d+)\s+lands\s+or\s+MDFC',
        ],
        'nonlands': [
            r'(\d+)\s+non-lands',
        ],
        'total_cards': [
            r'(\d+)\s+total cards imported',
        ],
        'avg_cmc': [
            r'Avg CMC\s+([\d.]+)',
        ],
        'avg_impact': [
            r'Avg Impact\s+([\d.]+)',
        ],
    }

    for key, pattern_list in patterns.items():
        for pattern in pattern_list:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = match.group(1)
                if key in ['score', 'tipping_point', 'lands', 'nonlands', 'total_cards', 'commander_bracket']:
                    results[key] = int(value)
                else:
                    results[key] = float(value)
                break

    return results


def format_output(deck_name, results, url=None):
    """Format results for Claude to read."""
    output = []
    output.append(f"DECK: {deck_name}")
    output.append("")

    if url:
        output.append(f"URL: {url}")
        output.append("")

    if not results:
        output.append("WARNING: No metrics extracted from page")
        return '\n'.join(output)

    # Primary Power Metrics
    if 'power_level' in results:
        output.append(f"POWER_LEVEL: {results['power_level']:.2f}/10")

    if 'commander_bracket' in results:
        output.append(f"COMMANDER_BRACKET: {results['commander_bracket']}")

    if 'efficiency' in results:
        output.append(f"EFFICIENCY: {results['efficiency']:.2f}/10")

    if 'score' in results:
        output.append(f"SCORE: {results['score']}/1000")

    if 'impact' in results:
        output.append(f"TOTAL_IMPACT: {results['impact']:.2f}")

    if 'avg_impact' in results:
        output.append(f"AVG_IMPACT: {results['avg_impact']:.2f}")

    if 'avg_playability' in results:
        output.append(f"AVG_PLAYABILITY: {results['avg_playability']:.1f}%")

    if 'tipping_point' in results:
        output.append(f"TIPPING_POINT: {results['tipping_point']}")

    output.append("")

    # Deck Composition
    if 'total_cards' in results:
        output.append(f"TOTAL_CARDS: {results['total_cards']}")

    if 'lands' in results:
        output.append(f"LANDS: {results['lands']}")

    if 'nonlands' in results:
        output.append(f"NONLANDS: {results['nonlands']}")

    if 'avg_cmc' in results:
        output.append(f"AVG_CMC: {results['avg_cmc']:.2f}")

    output.append("")

    # Mana Probabilities
    if 'mana_screw' in results:
        output.append(f"MANA_SCREW: {results['mana_screw']:.1f}%")

    if 'mana_flood' in results:
        output.append(f"MANA_FLOOD: {results['mana_flood']:.1f}%")

    if 'mana_optimal' in results:
        output.append(f"MANA_OPTIMAL: {results['mana_optimal']:.1f}%")

    return '\n'.join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_deck_url.py <deck_file>", file=sys.stderr)
        print("\nAvailable deck files:", file=sys.stderr)
        options_dir = Path(__file__).parent / "options"
        if options_dir.exists():
            for file in sorted(options_dir.glob("*.md")):
                print(f"  - {file.name}", file=sys.stderr)
        sys.exit(1)

    deck_file = sys.argv[1]

    # Check in options/ folder if file doesn't exist
    if not os.path.exists(deck_file):
        options_path = Path(__file__).parent / "options" / deck_file
        if options_path.exists():
            deck_file = str(options_path)
        else:
            print(f"ERROR: File not found: {deck_file}", file=sys.stderr)
            sys.exit(1)

    # Parse deck file
    cards = parse_deck_file(deck_file)
    deck_name = Path(deck_file).stem

    # Generate URL
    url = generate_url(cards)

    # Fetch page with JavaScript rendering
    print(f"Analyzing {deck_name}...", file=sys.stderr)
    text = fetch_with_playwright(url)

    # Parse results
    results = parse_results(text)

    # Output formatted results
    print(format_output(deck_name, results, url))


if __name__ == "__main__":
    main()
