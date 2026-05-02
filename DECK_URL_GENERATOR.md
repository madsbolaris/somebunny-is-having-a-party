# EDH Power Level Deck Analyzer

Analyzes Commander decks using [EDH Power Level](https://edhpowerlevel.com/) and returns power level metrics.

## Requirements

```bash
pip install playwright
playwright install chromium
```

## Files

- `options/` - Directory containing deck list files (one.md, two.md, three.md)
- `generate_deck_url.py` - Python script that analyzes a deck and returns power level metrics
- `analyze_deck.sh` - Simple bash wrapper for the Python script

## Deck File Format

Deck files should be in the following format:

```
1 Commander Name

12 Card Name
1 Another Card
1 Yet Another Card

1 Section Two Card
1 More Cards
```

- Each line contains a quantity and card name separated by a space
- Empty lines create section separators
- Card names can include spaces, commas, and apostrophes

## Usage

### Analyze a single deck

```bash
python3 generate_deck_url.py options/three.md
```

Or using the wrapper:

```bash
./analyze_deck.sh three.md
```

### Example Output

```
DECK: three

POWER_LEVEL: 8.84/10
COMMANDER_BRACKET: 4
EFFICIENCY: 7.49/10
SCORE: 870/1000
TOTAL_IMPACT: 881.06
AVG_IMPACT: 8.80
AVG_PLAYABILITY: 67.3%
TIPPING_POINT: 3

TOTAL_CARDS: 100
LANDS: 32
NONLANDS: 67
AVG_CMC: 2.63

MANA_SCREW: 41.3%
MANA_FLOOD: 18.1%
MANA_OPTIMAL: 40.6%
```

## Output Metrics

### Power Metrics
- **POWER_LEVEL**: Overall deck power rating (0-10 scale)
- **COMMANDER_BRACKET**: Official Commander bracket (1-5 scale, where 5 is cEDH)
- **EFFICIENCY**: How efficiently the deck operates (0-10 scale)
- **SCORE**: Composite performance score (0-1000 scale)
- **TOTAL_IMPACT**: Total impact value of all cards combined
- **AVG_IMPACT**: Average impact value per card
- **AVG_PLAYABILITY**: Average playability percentage across all cards
- **TIPPING_POINT**: Critical mana threshold (the CMC where the deck becomes functional)

### Deck Composition
- **TOTAL_CARDS**: Total number of cards in the deck
- **LANDS**: Number of lands (including MDFCs)
- **NONLANDS**: Number of nonland cards
- **AVG_CMC**: Average converted mana cost

### Mana Analysis
- **MANA_SCREW**: Probability of not drawing enough lands (lower is better)
- **MANA_FLOOD**: Probability of drawing too many lands (lower is better)
- **MANA_OPTIMAL**: Probability of optimal mana distribution (higher is better)

## How It Works

1. Parses deck file line by line
2. URL-encodes card names (spaces→`+`, commas→`%2C`, apostrophes→`%27`)
3. Generates edhpowerlevel.com URL
4. Uses Playwright to load the page and wait for JavaScript calculations
5. Extracts metrics from the rendered page
6. Outputs formatted results

## Deck Analysis Summary

All three variants are Baylen, the Haymaker bunny tribal decks at Commander Bracket 4 (Optimized):

### options/one.md
- Power: 8.92/10, Score: 880/1000
- 28 lands, AVG CMC: 2.67
- **Mana Issue**: 54.4% screw, 11.1% flood, 34.5% optimal
- Average Playability: 58.7%

### options/two.md (Highest Power)
- Power: 8.96/10, Score: 885/1000
- 28 lands, AVG CMC: 2.67
- **Mana Issue**: 54.4% screw, 11.1% flood, 34.5% optimal
- Average Playability: 58.5%

### options/three.md (Best Mana Base)
- Power: 8.84/10, Score: 870/1000
- 32 lands, AVG CMC: 2.63
- **Better Mana**: 41.3% screw, 18.1% flood, 40.6% optimal
- Average Playability: 67.3%

**Key Insight**: Deck three trades ~1% power for significantly better mana consistency (40.6% vs 34.5% optimal) and higher playability (67.3% vs ~58%). The 4 additional lands reduce mana screw by 13%.
