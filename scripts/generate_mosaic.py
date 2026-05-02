#!/usr/bin/env python3
"""
Generate a mosaic image of all cards in the deck.
Reads card printings from THEME_ANALYSIS.md and supports both B3 and B4 variants.

Downloads card images from Scryfall's image API (respecting their 75ms rate limit)
and composites them into a single large image.

Usage:
    python scripts/generate_mosaic.py        # Generate both B3 and B4 mosaics
    python scripts/generate_mosaic.py b4     # Generate B4 mosaic only
    python scripts/generate_mosaic.py b3     # Generate B3 mosaic only
"""

import sys
import re
import time
import math
import urllib.request
from pathlib import Path
from PIL import Image

REPO_DIR = Path(__file__).parent.parent
THEME_FILE = REPO_DIR / "THEME_ANALYSIS.md"
CACHE_DIR = REPO_DIR / "card_images"

# Scryfall asks for 50-100ms between requests
DELAY_BETWEEN_REQUESTS = 0.15  # 150ms to be safe

CARD_WIDTH = 488   # Scryfall "normal" size
CARD_HEIGHT = 680

# Layout order for B4 mosaic — sorted by color group, bunny cards first
ORDERED_NAMES_B4 = [
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
    "Carrot Cake",
    # Row 6: Colorless artifacts continued
    "Swiftfoot Boots",
    "Coat of Arms", "Sol Ring", "Arcane Signet",
    "Chrome Mox", "Skullclamp",
    *["Hare Apparent"] * 3,
    # Row 7: Hare Apparent continued + Cavern
    *["Hare Apparent"] * 9,
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

# Layout order for B3 mosaic — same structure, B3 cards swapped in
ORDERED_NAMES_B3 = [
    # Row 1: White creatures (bunnies first) + white artifacts/enchantments
    "Warren Warleader", "Harvestrite Host", "Regal Bunnicorn",
    "Head of the Homestead", "Valley Questcaller",
    "Byrke, Long Ear of the Law", "Druid of the Spade", "Mentor of the Meek",
    "Caretaker's Talent", "Halo Fountain",
    # Row 2: White instants/sorceries/enchantments (bunny art first)
    "Tocasia's Welcome",
    "Swords to Plowshares", "Hop to It", "Season of the Burrow",
    "Generous Gift", "Grand Crescendo", "Path to Exile",
    "Flawless Maneuver", "Unbreakable Formation",
    "Intangible Virtue",
    # Row 3: More white enchantments + green creatures (bunnies first)
    "Anointed Procession", "Cathars' Crusade", "Congregation at Dawn",
    "March of the Multitudes",
    "Craterhoof Behemoth", "Birds of Paradise",
    "Pawpatch Formation",
    "Chord of Calling", "Heroic Intervention",
    "Shamanic Revelation",
    # Row 4: Green sorceries + enchantments (bunny art first)
    "For the Common Good", "Second Harvest",
    "Natural Order", "Finale of Devastation",
    "Three Visits", "Nature's Lore", "Sylvan Tutor",
    "Sylvan Library", "Parallel Lives",
    # Row 5: More green enchantments + multicolor (bunnies first)
    "Doubling Season", "The Great Henge",
    "Baylen, the Haymaker",
    "Cadira, Caller of the Small", "Finneas, Ace Archer",
    "Eladamri's Call", "Aura Shards",
    "Jetmir, Nexus of Revels",
    "Boros Charm",
    "Carrot Cake",
    # Row 6: Colorless artifacts
    "Swiftfoot Boots",
    "Coat of Arms", "Sol Ring", "Arcane Signet",
    "Talisman of Unity", "Talisman of Impulse", "Skullclamp",
    *["Hare Apparent"] * 3,
    # Row 7: Hare Apparent continued + Cavern
    *["Hare Apparent"] * 9,
    "Cavern of Souls",
    # Row 8: Modern lands — shocks + checklands + utility
    "Temple Garden", "Sacred Foundry", "Stomping Ground",
    "Bountiful Promenade", "Sunpetal Grove", "Brushland",
    "The Shire", "Castle Garenbrig", "Gavony Township",
    "Wasteland",
    # Row 9: Lands continued
    "Windswept Heath", "Wooded Foothills", "Arid Mesa",
    "Horizon Canopy", "Inspiring Vantage",
    "Wooded Bastion", "Jetmir's Garden",
    "Reflecting Pool", "Exotic Orchard", "Command Tower",
    # Row 10: Channel lands + five-color + duals
    "Yavimaya, Cradle of Growth", "Boseiju, Who Endures",
    "Eiganjo, Seat of the Empire",
    "Mana Confluence", "City of Brass",
    "Gaea's Cradle",
    "Savannah", "Plateau", "Taiga",
]


def extract_scryfall_urls(theme_file: Path, variant: str) -> list[tuple[str, str, bool]]:
    """Extract (card_name, scryfall_page_url, has_rabbit_art) from the theme analysis markdown.
    
    Filters to cards matching the given variant: includes 'Both' + the variant-specific cards.
    """
    content = theme_file.read_text()
    # Match table rows: | Card Name | Deck | [🔗](url) | Rabbit? | Rabbit Art? | ...
    pattern = re.compile(
        r'\|\s*([^|]+?)\s*\|\s*(\w+)\s*\|\s*\[🔗\]\((https://scryfall\.com/card/[^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
    )
    
    variant_upper = variant.upper()  # "B3" or "B4"
    valid_decks = {"Both", variant_upper}
    
    results = []
    seen = set()
    for match in pattern.finditer(content):
        name = match.group(1).strip().split(" ×")[0]  # Handle "Hare Apparent ×12"
        deck = match.group(2).strip()
        url = match.group(3)
        is_rabbit = "✅" in match.group(4)
        has_rabbit_art = "✅" in match.group(5)
        has_bunny = is_rabbit or has_rabbit_art
        
        if deck not in valid_decks:
            continue
        if name not in seen:
            seen.add(name)
            results.append((name, url, has_bunny))
    
    # Build a name→(url, bunny) lookup
    card_map = {c[0]: (c[1], c[2]) for c in results}
    
    ordered_names = ORDERED_NAMES_B4 if variant_upper == "B4" else ORDERED_NAMES_B3
    
    # Build final list from the ordered names
    expanded = []
    for name in ordered_names:
        if name in card_map:
            url, bunny = card_map[name]
            expanded.append((name, url, bunny))
        else:
            print(f"  WARNING: '{name}' not found in theme analysis for {variant_upper}")
    
    # Safety: add any cards from the theme analysis that we missed in the manual order
    ordered_set = set(ordered_names)
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


def generate_variant(variant: str):
    """Generate a mosaic for a single variant (b3 or b4)."""
    output_file = REPO_DIR / f"deck_mosaic_{variant}.png"
    
    print(f"\n{'='*60}")
    print(f"Generating {variant.upper()} mosaic...")
    print(f"{'='*60}")
    
    print("Extracting card URLs from theme analysis...")
    cards = extract_scryfall_urls(THEME_FILE, variant)
    bunny_count = sum(1 for c in cards if c[2])
    print(f"Found {len(cards)} cards ({bunny_count} with bunnies)")
    
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
    w, h, rows, cols = create_mosaic(image_paths, output_file, cols=10)
    print(f"Done! {variant.upper()} mosaic: {w}x{h} ({cols} cols × {rows} rows)")
    print(f"Saved to: {output_file}")


def main():
    variants = sys.argv[1:] if len(sys.argv) > 1 else ["b4", "b3"]
    for v in variants:
        if v.lower() not in ("b3", "b4"):
            print(f"Unknown variant '{v}'. Use 'b3' or 'b4'.")
            sys.exit(1)
    for v in variants:
        generate_variant(v.lower())


if __name__ == "__main__":
    main()
