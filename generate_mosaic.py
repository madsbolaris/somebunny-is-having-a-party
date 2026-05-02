#!/usr/bin/env python3
"""
Generate a mosaic image of all cards in the B4 deck.
Uses the specific printings chosen in BRACKET_4_THEME_ANALYSIS.md.

Downloads card images from Scryfall's image API (respecting their 75ms rate limit)
and composites them into a single large image.
"""

import os
import re
import time
import math
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image
from io import BytesIO

SCRIPT_DIR = Path(__file__).parent
THEME_FILE = SCRIPT_DIR / "BRACKET_4_THEME_ANALYSIS.md"
CACHE_DIR = SCRIPT_DIR / "card_images"
OUTPUT_FILE = SCRIPT_DIR / "deck_mosaic.png"

# Scryfall asks for 50-100ms between requests
DELAY_BETWEEN_REQUESTS = 0.15  # 150ms to be safe

CARD_WIDTH = 488   # Scryfall "normal" size
CARD_HEIGHT = 680


def extract_scryfall_urls(theme_file: Path) -> list[tuple[str, str, bool]]:
    """Extract (card_name, scryfall_page_url, has_rabbit_art) from the theme analysis markdown."""
    content = theme_file.read_text()
    # Match table rows: | Card Name | SET | [🔗](url) | Rabbit? | Rabbit Art? | ...
    pattern = re.compile(
        r'\|\s*([^|]+?)\s*\|\s*\w+\s*\|\s*\[🔗\]\((https://scryfall\.com/card/[^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
    )
    results = []
    seen = set()
    for match in pattern.finditer(content):
        name = match.group(1).strip().split(" ×")[0]  # Handle "Hare Apparent ×12"
        url = match.group(2)
        is_rabbit = "✅" in match.group(3)
        has_rabbit_art = "✅" in match.group(4)
        has_bunny = is_rabbit or has_rabbit_art
        if name not in seen:
            seen.add(name)
            results.append((name, url, has_bunny))
    
    # Build a name→(url, bunny) lookup
    card_map = {c[0]: (c[1], c[2]) for c in results}
    
    # Layout: sorted by color group, bunny cards first within each group
    # Reserved list / old-border cards at the bottom
    ordered_names = [
        # Row 1: White creatures (bunnies first) + white artifacts/enchantments
        "Warren Warleader", "Harvestrite Host", "Regal Bunnicorn",
        "Head of the Homestead", "Valley Questcaller",
        "Byrke, Long Ear of the Law", "Mentor of the Meek",
        "Caretaker's Talent", "Halo Fountain", "Tocasia's Welcome",
        # Row 2: White instants/sorceries/enchantments (bunny art first)
        "Swords to Plowshares", "Hop to It", "Season of the Burrow",
        "Generous Gift", "Grand Crescendo", "Path to Exile",
        "Teferi's Protection", "Unbreakable Formation",
        "Smothering Tithe", "Intangible Virtue",
        # Row 3: More white enchantments + green creatures (bunnies first)
        "Anointed Procession", "Cathars' Crusade", "Enlightened Tutor",
        "March of the Multitudes",
        "Craterhoof Behemoth", "Birds of Paradise",
        # Green instants (bunny art first)
        "Pawpatch Formation",
        "Chord of Calling", "Heroic Intervention",
        "Shamanic Revelation",
        # Row 4: Green sorceries + enchantments (bunny art first)
        "For the Common Good", "Second Harvest",
        "Natural Order", "Finale of Devastation",
        "Three Visits", "Nature's Lore", "Worldly Tutor",
        "Sylvan Library", "Parallel Lives",
        # Row 5: More green enchantments + multicolor (bunnies first)
        "Doubling Season", "The Great Henge",
        "Baylen, the Haymaker",
        "Cadira, Caller of the Small", "Finneas, Ace Archer",
        "Eladamri's Call", "Aura Shards",
        "Jetmir, Nexus of Revels",
        "Boros Charm",
        # Colorless artifacts (bunny art first)
        "Carrot Cake",
        # Row 6: Colorless artifacts continued
        "Swiftfoot Boots",
        "Coat of Arms", "Sol Ring", "Arcane Signet",
        "Chrome Mox", "Skullclamp",
        # 12 Hare Apparent
        *["Hare Apparent"] * 3,
        # Row 7: Hare Apparent continued
        *["Hare Apparent"] * 9,
        # Lands start
        "Cavern of Souls",
        # Row 8: Modern lands — shocks + checklands + utility
        "Temple Garden", "Sacred Foundry", "Stomping Ground",
        "Bountiful Promenade", "Sunpetal Grove", "Brushland",
        "The Shire", "Castle Garenbrig", "Gavony Township",
        "Wasteland",
        # Row 9: Fetches + mana-fixing lands
        "Windswept Heath", "Wooded Foothills", "Arid Mesa",
        "Misty Rainforest", "Flooded Strand",
        "Verdant Catacombs", "Bloodstained Mire",
        "Reflecting Pool", "Exotic Orchard", "Command Tower",
        # Row 10: Channel lands + five-color + reserved list / old border
        "Yavimaya, Cradle of Growth", "Boseiju, Who Endures",
        "Eiganjo, Seat of the Empire",
        "Mana Confluence", "City of Brass",
        "Ancient Tomb",
        "Mox Diamond", "Survival of the Fittest",
        "Gaea's Cradle",
        "Savannah", "Plateau", "Taiga",
    ]
    
    # Build final list from the ordered names
    expanded = []
    for name in ordered_names:
        if name in card_map:
            url, bunny = card_map[name]
            expanded.append((name, url, bunny))
        else:
            print(f"  WARNING: '{name}' not found in theme analysis")
    
    # Safety: add any cards from the theme analysis that we missed in the manual order
    ordered_set = set()
    for name in ordered_names:
        ordered_set.add(name)
    for name, url, bunny in results:
        if name not in ordered_set:
            print(f"  WARNING: '{name}' not in manual order, appending at end")
            expanded.append((name, url, bunny))
    
    return expanded


def scryfall_page_to_image_url(page_url: str) -> str:
    """Convert a scryfall page URL to the image download URL.
    
    e.g. https://scryfall.com/card/blb/205/baylen-the-haymaker
      -> https://api.scryfall.com/cards/blb/205?format=image&version=normal
    """
    # Extract set/number from URL path
    parts = page_url.rstrip("/").split("/card/")[1].split("/")
    set_code = parts[0]
    collector_number = parts[1]
    return f"https://api.scryfall.com/cards/{set_code}/{collector_number}?format=image&version=normal"


def download_image(url: str, cache_path: Path) -> Path:
    """Download an image, using cache to avoid re-downloads."""
    if cache_path.exists():
        return cache_path
    
    req = urllib.request.Request(url, headers={
        "User-Agent": "DeckMosaic/1.0 (contact: deck-builder)",
        "Accept": "image/*"
    })
    resp = urllib.request.urlopen(req)
    data = resp.read()
    cache_path.write_bytes(data)
    return cache_path


def create_mosaic(image_paths: list[Path], output: Path, cols: int = 10):
    """Combine card images into a grid mosaic."""
    images = []
    for p in image_paths:
        img = Image.open(p)
        # Resize to standard dimensions if needed
        if img.size != (CARD_WIDTH, CARD_HEIGHT):
            img = img.resize((CARD_WIDTH, CARD_HEIGHT), Image.LANCZOS)
        images.append(img)
    
    rows = math.ceil(len(images) / cols)
    mosaic_w = cols * CARD_WIDTH
    mosaic_h = rows * CARD_HEIGHT
    
    mosaic = Image.new("RGB", (mosaic_w, mosaic_h), (30, 30, 30))
    
    for i, img in enumerate(images):
        row = i // cols
        col = i % cols
        mosaic.paste(img, (col * CARD_WIDTH, row * CARD_HEIGHT))
    
    mosaic.save(output, "PNG", optimize=True)
    return mosaic_w, mosaic_h, rows, cols


def main():
    print("Extracting card URLs from theme analysis...")
    cards = extract_scryfall_urls(THEME_FILE)
    bunny_count = sum(1 for c in cards if c[2])
    print(f"Found {len(cards)} unique cards ({bunny_count} with bunnies, shown first)")
    
    CACHE_DIR.mkdir(exist_ok=True)
    
    image_paths = []
    for i, (name, page_url, has_bunny) in enumerate(cards):
        img_url = scryfall_page_to_image_url(page_url)
        # Safe filename from set/collector
        parts = page_url.rstrip("/").split("/card/")[1].split("/")
        cache_name = f"{parts[0]}_{parts[1]}.jpg"
        cache_path = CACHE_DIR / cache_name
        
        status = "cached" if cache_path.exists() else "downloading"
        bunny_marker = " 🐰" if has_bunny else ""
        print(f"  [{i+1}/{len(cards)}] {name} ({status}){bunny_marker}")
        
        try:
            download_image(img_url, cache_path)
            image_paths.append(cache_path)
        except Exception as e:
            print(f"    ERROR: {e}")
            continue
        
        # Only delay if we actually downloaded (not cached)
        if status == "downloading":
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    print(f"\nAssembling mosaic from {len(image_paths)} images...")
    # 10 columns gives a nice layout for 89 cards (9 rows)
    w, h, rows, cols = create_mosaic(image_paths, OUTPUT_FILE, cols=10)
    print(f"Done! Mosaic: {w}x{h} ({cols} cols × {rows} rows)")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
