# MTG Commander Deck Scoring Calculator

## Purpose

This document provides detailed scoring rubrics for each of the **8 quantitative metrics** used in Phase 3 of the evaluation process. Use these tables to convert your observations from Phase 2 into numerical scores (1-10).

---

## Table of Contents

1. [Speed Score](#1-speed-score)
2. [Mana Base Quality Score](#2-mana-base-quality-score)
3. [Fast Mana Density Score](#3-fast-mana-density-score)
4. [Card Draw/Advantage Score](#4-card-drawadvantage-score)
5. [Interaction Quality Score](#5-interaction-quality-score)
6. [Synergy Density Score](#6-synergy-density-score)
7. [Threat Density Score](#7-threat-density-score)
8. [Resilience Score](#8-resilience-score)
9. [Weighted Scorecard Calculation](#weighted-scorecard-calculation)
10. [Quick Reference Tables](#quick-reference-tables)

---

## 1. Speed Score

**Metric**: Average win turn from Phase 1 goldfish testing

**Weight in Final Score**: 20%

### Scoring Table

| Score | Win Turn Range | Description |
|-------|----------------|-------------|
| **10** | Turn 2-3 | Explosive fast combo, cEDH tier, can threaten turn 1-2 in perfect scenarios |
| **9** | Turn 4 | Very fast combo or highly aggressive, fringe to full cEDH |
| **8** | Turn 5-6 | Fast combo or optimized aggressive strategy, high power |
| **7** | Turn 7-8 | Focused midrange or tuned combo, high power to optimized |
| **6** | Turn 9-10 | Solid focused strategy, upper end of casual play |
| **5** | Turn 11-12 | Moderate speed, mid-tier casual |
| **4** | Turn 13-14 | Slower casual strategies, upgraded precons |
| **3** | Turn 15-16 | Very slow, basic precons or unfocused builds |
| **2** | Turn 17-18 | Extremely slow, struggles to close games |
| **1** | Turn 19+ | Rarely wins, no clear closer, precon or worse |

### Calculation Method

1. Goldfish the deck 3-5 times (no opponent interaction)
2. Record the turn number where the deck would secure victory
3. Calculate the average win turn
4. Match the average to the table above

### Examples

- **Score 10**: Godo Helm combo consistently wins turn 3, can win turn 2 with perfect draw
- **Score 8**: Kinnan Bonder Prodigy generates infinite mana and wins turn 5-6
- **Score 6**: Edgar Markov vampire tribal establishes overwhelming board turn 9-10
- **Score 4**: Upgraded dragon tribal precon wins turn 13-14 through combat
- **Score 2**: Unmodified 2020 precon struggles to close, wins turn 17-18 if at all

---

## 2. Mana Base Quality Score

**Metric**: Percentage of lands that are Tier 1-2 (untapped, good fixing) + total land count

**Weight in Final Score**: 15%

### Scoring Table

| Score | Land Count | Tier 1-2 % | Description |
|-------|-----------|------------|-------------|
| **10** | 30-33 | 80%+ | Perfect mana base: fetches, ABUR duals, shocks, optimal count |
| **9** | 32-34 | 70-80% | Excellent mana base: mostly optimized lands |
| **8** | 34-35 | 60-70% | Very good mana base: good fixing, few tap lands |
| **7** | 35-36 | 50-60% | Good mana base: solid fixing, some tap lands |
| **6** | 36-37 | 40-50% | Decent mana base: basic fixing, mix of tap/untapped |
| **5** | 37-38 | 30-40% | Moderate mana base: limited fixing, many tap lands |
| **4** | 38-39 | 20-30% | Weak mana base: poor fixing, mostly tap lands |
| **3** | 39-40 | 10-20% | Very weak: almost all tap lands and basics |
| **2** | 40+ | <10% | Poor: all tap lands and basics, no fixing |
| **1** | 40+ | 0% | Terrible: all basics or all tap lands, no fixing |

### Land Quality Tiers (for reference)

**Tier 1 - Premium Lands**:
- ABUR Duals (Tropical Island, Underground Sea, etc.)
- Fetch Lands (Scalding Tarn, Misty Rainforest, etc.)
- Shock Lands (Steam Vents, Breeding Pool, etc.)
- Fast Mana Lands (Ancient Tomb, Mana Confluence, City of Brass)
- Key Utility Lands (Boseiju, Cavern of Souls, Strip Mine)

**Tier 2 - Good Lands**:
- Filter Lands (Cascade Bluffs, Mystic Gate, etc.)
- Pain Lands (Adarkar Wastes, Underground River, etc.)
- Check Lands (Glacial Fortress, Dragonskull Summit, etc.)
- Horizon Lands (Horizon Canopy, Fiery Islet, etc.)
- Fast Lands (Spirebluff Canal, Blooming Marsh, etc.)

**Tier 3 - Decent Lands**:
- Tango/Battle Lands (Prairie Stream, Cinder Glade, etc.)
- Slow Fetches (Terramorphic Expanse, Evolving Wilds)
- Bounce/Karoo Lands (Simic Growth Chamber, etc.)
- Pathways (Barkchannel Pathway, etc.)

**Tier 4 - Budget/Weak Lands**:
- Gain Lands (Tranquil Cove, Dismal Backwater, etc.)
- Tri-lands that enter tapped (Arcane Sanctum, etc.)
- Gates
- Basic Lands

### Calculation Method

1. Count total lands
2. Count lands in each tier
3. Calculate Tier 1-2 percentage: (Tier 1 + Tier 2) / Total Lands × 100%
4. Match land count and percentage to table above
5. If between two scores, round based on context (better fixing = round up)

### Examples

- **Score 10**: 31 lands, 26 are Tier 1-2 (84%), includes ABUR duals and fetches
- **Score 7**: 36 lands, 18 are Tier 1-2 (50%), mix of checks/pains and tap lands
- **Score 4**: 38 lands, 8 are Tier 1-2 (21%), mostly gainlands and basics
- **Score 1**: 42 lands, all basics, no color fixing

---

## 3. Fast Mana Density Score

**Metric**: Number of fast mana pieces (0-2 CMC ramp)

**Weight in Final Score**: 10%

### Scoring Table

| Score | Fast Mana Pieces | Description |
|-------|------------------|-------------|
| **10** | 8+ | Extreme fast mana: cEDH level, multiple 0-CMC pieces |
| **9** | 6-7 | Very high fast mana: high power to cEDH, competitive density |
| **8** | 5 | High fast mana: high power, very explosive starts |
| **7** | 4 | Good fast mana: optimized casual to high power |
| **6** | 3 | Moderate fast mana: focused casual |
| **5** | 2 | Low fast mana: basic optimization |
| **4** | 1 | Minimal fast mana: Sol Ring + inefficient ramp |
| **3** | 1 | Sol Ring + slow ramp only |
| **2** | 1 | Sol Ring only, no other fast mana |
| **1** | 0 | No fast mana at all |

### Fast Mana Categories

**0 CMC (Tier 1)**:
- Mana Crypt
- Mox Diamond
- Chrome Mox
- Jeweled Lotus
- Lion's Eye Diamond
- Lotus Petal

**1 CMC (Tier 2)**:
- Sol Ring
- Mana Vault
- Dark Ritual
- Elvish Mystic
- Birds of Paradise
- Noble Hierarch
- Carpet of Flowers

**2 CMC (Tier 3)**:
- Arcane Signet
- All Signets (Azorius, Dimir, etc.)
- All Talismans (Talisman of Progress, etc.)
- Fellwar Stone
- Nature's Lore
- Three Visits
- Farseek
- Rampant Growth

### Calculation Method

1. List all ramp spells with CMC 0-2
2. Count the total
3. Match to table above

### Examples

- **Score 10**: Mana Crypt, Mox Diamond, Chrome Mox, Jeweled Lotus, Sol Ring, Mana Vault, 2 signets = 8 pieces
- **Score 7**: Sol Ring, Arcane Signet, 2 signets = 4 pieces
- **Score 5**: Sol Ring, Arcane Signet = 2 pieces
- **Score 2**: Sol Ring only

---

## 4. Card Draw/Advantage Score

**Metric**: Number of card draw sources + number of tutors

**Weight in Final Score**: 15%

### Scoring Table

| Score | Draw Sources | Tutors | Description |
|-------|--------------|--------|-------------|
| **10** | 15+ | 6+ | Extreme card advantage: wheels, tutors, perfect selection |
| **9** | 12-14 | 5-6 | Excellent card advantage: great engines and tutors |
| **8** | 10-12 | 3-4 | Very good card advantage: strong engines, several tutors |
| **7** | 9-10 | 2-3 | Good card advantage: solid engines, some tutors |
| **6** | 7-8 | 1-2 | Decent card advantage: moderate engines, limited tutors |
| **5** | 6-7 | 0-1 | Moderate card advantage: basic engines, minimal tutors |
| **4** | 4-5 | 0 | Limited card advantage: few sources, no tutors |
| **3** | 3 | 0 | Very limited: struggling to refill hand |
| **2** | 1-2 | 0 | Minimal card advantage: will run out of gas |
| **1** | 0-1 | 0 | No card advantage: top-deck mode constantly |

### Card Draw Categories

**Burst Draw** (one-time large draws):
- Wheels: Wheel of Fortune, Windfall, etc.
- Large draws: Blue Sun's Zenith, Pull from Tomorrow, etc.

**Incremental Draw** (ongoing engines):
- Rhystic Study, Mystic Remora, Phyrexian Arena, Sylvan Library
- The One Ring, Esper Sentinel, Sensei's Divining Top
- Dark Confidant, Ledger Shredder, Consecrated Sphinx, Tymna

**Tutors** (any card that searches library):
- Demonic Tutor, Vampiric Tutor, Mystical Tutor, Worldly Tutor
- Enlightened Tutor, Gamble, Merchant Scroll
- Chord of Calling, Eladamri's Call

### Calculation Method

1. Count all sources of card draw (burst + incremental)
2. Count all tutors separately
3. Match both numbers to table above
4. If between rows, favor the category with more weight (draw > tutors for most decks)

### Examples

- **Score 10**: 16 draw sources (4 wheels, 8 engines, 4 selection pieces) + 7 tutors
- **Score 7**: 9 draw sources (Rhystic Study, Sylvan Library, 7 others) + 3 tutors (Demonic, Vampiric, Worldly)
- **Score 4**: 5 draw sources (Harmonize, Read the Bones, 3 conditional triggers) + 0 tutors
- **Score 1**: 1 draw source (Commander's ability only) + 0 tutors

---

## 5. Interaction Quality Score

**Metric**: Number of interaction pieces + efficiency + speed + coverage

**Weight in Final Score**: 15%

### Scoring Table

| Score | Pieces | Avg CMC | Instant % | Coverage | Description |
|-------|--------|---------|-----------|----------|-------------|
| **10** | 15+ | 0-1 | 80%+ | Full | Free spells, perfect efficiency, complete coverage |
| **9** | 12-14 | 1-2 | 70%+ | Full | Mostly efficient, mostly instant, excellent coverage |
| **8** | 10-12 | 1.5-2.5 | 60%+ | Good | Good efficiency, good instant speed, good coverage |
| **7** | 9-10 | 2-3 | 50%+ | Good | Moderate efficiency, some instant speed, solid coverage |
| **6** | 7-8 | 2.5-3.5 | 40%+ | Decent | Mix of speeds/efficiency, decent coverage |
| **5** | 6-7 | 3-4 | 30%+ | Basic | Mostly sorcery, basic coverage |
| **4** | 4-5 | 4+ | 20%+ | Limited | Expensive, slow, limited coverage |
| **3** | 3 | 4+ | 10%+ | Narrow | Very expensive, very slow, narrow coverage |
| **2** | 1-2 | 5+ | 0% | Minimal | Almost no interaction |
| **1** | 0-1 | N/A | 0% | None | No interaction |

### Interaction Categories

**Spot Removal**:
- Swords to Plowshares, Path to Exile, Fatal Push, Beast Within, Generous Gift

**Board Wipes**:
- Wrath of God, Damnation, Toxic Deluge, Cyclonic Rift (overloaded)

**Counterspells**:
- Force of Will, Counterspell, Swan Song, Mana Drain

**Targeted Permanent Removal**:
- Nature's Claim, Wear // Tear, Fragmentize

**Stax**:
- Winter Orb, Trinisphere, Thalia

### Efficiency Reference

- **0-1 CMC**: Force of Will, Swords to Plowshares, Fatal Push
- **2 CMC**: Counterspell, Cyclonic Rift, Assassin's Trophy
- **3 CMC**: Beast Within, Toxic Deluge, Generous Gift
- **4+ CMC**: Supreme Verdict, Merciless Eviction (expensive)

### Coverage Assessment

Check all types the deck can answer:
- [ ] Creatures
- [ ] Artifacts
- [ ] Enchantments
- [ ] Planeswalkers
- [ ] Stack (counterspells)
- [ ] Graveyard

**Full coverage** = 5-6 types
**Good coverage** = 4 types
**Decent coverage** = 3 types
**Limited coverage** = 2 types
**Narrow coverage** = 1 type

### Calculation Method

1. Count all interaction pieces
2. Calculate average CMC of interaction
3. Calculate % that are instant speed
4. Assess coverage (how many permanent types can be answered)
5. Match to table above

### Examples

- **Score 10**: 16 pieces (Force of Will, Force of Negation, Swords, Path, etc.), avg CMC 1.1, 85% instant, full coverage
- **Score 7**: 10 pieces (Counterspell, Beast Within, Swords, Wrath, etc.), avg CMC 2.7, 60% instant, good coverage
- **Score 4**: 5 pieces (Murder, Naturalize, Cancel, etc.), avg CMC 4.2, 20% instant, limited coverage
- **Score 1**: 1 piece (Doom Blade), no coverage diversity

---

## 6. Synergy Density Score

**Metric**: Percentage of cards in Tier 1-2 (core/strong synergy)

**Weight in Final Score**: 10%

### Scoring Table

| Score | Tier 1-2 % | Description |
|-------|-----------|-------------|
| **10** | 90%+ | Perfect focus: nearly every card is core to strategy |
| **9** | 80-89% | Excellent focus: minimal filler, extremely cohesive |
| **8** | 70-79% | Very strong focus: very little filler, highly cohesive |
| **7** | 60-69% | Strong focus: some filler, good cohesion |
| **6** | 50-59% | Moderate focus: decent cohesion, moderate filler |
| **5** | 40-49% | Loose focus: significant filler, loose cohesion |
| **4** | 30-39% | Unfocused: many fillers, unclear strategy |
| **3** | 20-29% | Very unfocused: mostly filler, scattered strategy |
| **2** | 10-19% | Extremely unfocused: almost all filler |
| **1** | <10% | No coherent strategy: pure goodstuff pile |

### Synergy Tier Definitions (for reference)

**Tier 1 - Core (9-10/10 synergy)**:
- Essential to primary strategy
- High synergy with multiple other cards
- Directly advances or completes win condition

**Tier 2 - Strong (7-8/10 synergy)**:
- Significant contribution to strategy
- Good synergy with several cards
- Strong support for win conditions

**Tier 3 - Support (5-6/10 synergy)**:
- Helpful but not critical
- Moderate synergy
- General utility that aids strategy

**Tier 4 - Weak (3-4/10 synergy)**:
- Minimal synergy with deck theme
- Generic "good stuff" cards

**Tier 5 - Filler (1-2/10 synergy)**:
- No meaningful synergy
- Low impact on game plan

### Calculation Method

1. Classify each non-land card into tiers 1-5 based on synergy
2. Count cards in Tier 1 and Tier 2
3. Calculate percentage: (Tier 1 + Tier 2) / (Total non-land cards) × 100%
4. Match to table above

### Examples

- **Score 10**: cEDH Godo Helm - 88 of 99 non-land cards (89%) are Tier 1-2 (all tutors, fast mana, protection, and combo pieces)
- **Score 7**: Optimized Edgar Markov - 40 of 60 non-land cards (67%) are Tier 1-2 (vampire synergies, but some generic removal)
- **Score 4**: Unfocused "dragons and spells" deck - 22 of 62 non-land cards (35%) are Tier 1-2
- **Score 1**: Random goodstuff pile - 5 of 60 non-land cards (8%) have any synergy

---

## 7. Threat Density Score

**Metric**: Number of win conditions + redundancy + compactness

**Weight in Final Score**: 10%

### Scoring Table

| Score | Win Conditions | Compactness | Redundancy | Description |
|-------|----------------|-------------|------------|-------------|
| **10** | 5+ | 2-card | Extreme | Multiple compact combos, massive redundancy, tutors for everything |
| **9** | 4 | 2-card | High | Several compact combos, high redundancy, many tutors |
| **8** | 3 | 2-3 card | Good | Multiple win cons, mix of compact/efficient, good redundancy |
| **7** | 2-3 | 2-3 card | Moderate | 2-3 win cons, reasonably compact, moderate redundancy |
| **6** | 2 | 3-card | Some | 2 win cons, moderate compactness, some redundancy |
| **5** | 2 | 3-4 card | Limited | 2 win cons, less compact, limited redundancy |
| **4** | 1-2 | 4+ card | Minimal | 1 primary + weak backup, elaborate, minimal redundancy |
| **3** | 1 | 4+ card | None | 1 win con with slight redundancy, elaborate |
| **2** | 1 | Unclear | None | 1 linear win con, no backup |
| **1** | 0-1 | Unclear | None | Unclear or extremely slow win condition |

### Compactness Definitions

- **2-card combo**: Demonic Consultation + Thassa's Oracle, Basalt Monolith + Rings of Brighthearth
- **3-card combo**: Many traditional combos
- **4+ card combo**: Elaborate Rube Goldberg machines
- **Combat**: Craterhoof + board, Voltron
- **Value grind**: Out-resource opponents over time

### Redundancy Assessment

**Extreme** (10): 6+ tutors, functional reprints of all key pieces, can win with primary pieces exiled

**High** (9): 5-6 tutors, functional reprints of most key pieces, strong backup if primary fails

**Good** (8): 4 tutors, some functional reprints, can pivot if primary disrupted

**Moderate** (7): 2-3 tutors, limited functional reprints

**Some** (6): 1-2 tutors, minimal reprints

**Limited** (5): 0-1 tutors, no reprints

**Minimal** (4): 0 tutors, single path to victory

**None** (1-3): No tutors, no backups

### Calculation Method

1. Count distinct win conditions
2. Assess compactness (how many cards needed for each)
3. Assess redundancy (tutors + functional reprints)
4. Match to table above

### Examples

- **Score 10**: cEDH Thrasios/Tymna - 6 win cons (Consultation/Pact + Oracle/Lab Man, IsoRev, others), all 2-card, 8 tutors
- **Score 7**: Kinnan Bonder Prodigy - 3 win cons (infinite mana + outlet, oracle, combat), 2-3 card combos, 4 tutors
- **Score 4**: Dragon tribal - 2 win cons (Craterhoof, combat), 4+ cards needed, 0 tutors
- **Score 1**: Precon - unclear win con, no tutors, no redundancy

---

## 8. Resilience Score

**Metric**: Protection effects + recursion + recovery mechanisms

**Weight in Final Score**: 5%

### Scoring Table

| Score | Protection | Recursion | Recovery | Description |
|-------|-----------|-----------|----------|-------------|
| **10** | Extensive | Perfect | Immediate | Near-impossible to disrupt, instant protection, perfect recursion |
| **9** | Very High | Excellent | Fast | Extensive protection (free counters, hexproof), excellent recursion |
| **8** | High | Good | Fast | Strong protection suite, good recursion, rebuilds quickly |
| **7** | Good | Some | Moderate | Solid protection, some recursion, can recover with time |
| **6** | Moderate | Limited | Slow | Moderate protection, limited recursion, slow recovery |
| **5** | Basic | Minimal | Slow | Basic protection, minimal recursion, struggles after disruption |
| **4** | Minimal | None | Very Slow | Minimal protection, no recursion, very vulnerable |
| **3** | Very Little | None | None | Very little protection, collapses to single board wipe |
| **2** | Almost None | None | None | Almost no protection, extremely fragile |
| **1** | None | None | None | No protection or resilience, folds to any interaction |

### Protection Categories

**Free Protection (highest value)**:
- Force of Will, Force of Negation, Pact of Negation, Fierce Guardianship

**Efficient Protection**:
- Counterspell, Swan Song, Lightning Greaves, Swiftfoot Boots

**Moderate Protection**:
- Heroic Intervention, Teferi's Protection, Diplomatic Immunity

### Recursion Categories

**Excellent** (9-10):
- Multiple recursion pieces (Eternal Witness, Regrowth, Noxious Revival, reanimation spells)
- Can recur from graveyard repeatedly

**Good** (7-8):
- 3-4 recursion pieces
- Can recover some key cards

**Some** (6-7):
- 1-2 recursion pieces
- Limited recovery

**Minimal/None** (1-5):
- 0-1 recursion pieces or none
- Cannot recover from major disruption

### Recovery Assessment

**Immediate/Fast** (9-10): Can rebuild same turn or next turn after board wipe

**Moderate** (6-8): Can rebuild within 2-3 turns

**Slow** (4-5): Requires 4+ turns to rebuild

**Very Slow/None** (1-3): Cannot effectively rebuild, game is over after disruption

### Calculation Method

1. Count protection effects (counterspells for own plays, hexproof, indestructible)
2. Count recursion pieces (graveyard retrieval, reanimation)
3. Assess recovery speed (how quickly can deck rebuild after board wipe)
4. Match to table above

### Examples

- **Score 10**: 8 free counters, 6 recursion pieces, can combo off from empty board, indestructible permanents
- **Score 7**: 4 counterspells, 2 recursion pieces (Eternal Witness, Regrowth), can rebuild in 2-3 turns
- **Score 4**: 1 protection spell (Heroic Intervention), 0 recursion, struggles to rebuild
- **Score 1**: 0 protection, 0 recursion, collapses to single board wipe

---

## Weighted Scorecard Calculation

### Step-by-Step Calculation

**Step 1**: Record all 8 metric scores

| Metric | Score (1-10) |
|--------|--------------|
| Speed | |
| Mana Base Quality | |
| Fast Mana Density | |
| Card Draw/Advantage | |
| Interaction Quality | |
| Synergy Density | |
| Threat Density | |
| Resilience | |

**Step 2**: Apply weights

| Metric | Weight | Score | Weighted Score |
|--------|--------|-------|----------------|
| Speed | 20% (0.20) | [A] | [A] × 0.20 = |
| Mana Base Quality | 15% (0.15) | [B] | [B] × 0.15 = |
| Fast Mana Density | 10% (0.10) | [C] | [C] × 0.10 = |
| Card Draw/Advantage | 15% (0.15) | [D] | [D] × 0.15 = |
| Interaction Quality | 15% (0.15) | [E] | [E] × 0.15 = |
| Synergy Density | 10% (0.10) | [F] | [F] × 0.10 = |
| Threat Density | 10% (0.10) | [G] | [G] × 0.10 = |
| Resilience | 5% (0.05) | [H] | [H] × 0.05 = |

**Step 3**: Sum weighted scores

**Total Weighted Score** = Sum of all weighted scores = _____/10

This is your **quantitative base rating** before qualitative adjustments.

### Example Calculation

**Example Deck: Optimized Kinnan**

| Metric | Weight | Score | Calculation | Weighted Score |
|--------|--------|-------|-------------|----------------|
| Speed | 20% | 8 | 8 × 0.20 | 1.60 |
| Mana Base Quality | 15% | 7 | 7 × 0.15 | 1.05 |
| Fast Mana Density | 10% | 6 | 6 × 0.10 | 0.60 |
| Card Draw/Advantage | 15% | 8 | 8 × 0.15 | 1.20 |
| Interaction Quality | 15% | 7 | 7 × 0.15 | 1.05 |
| Synergy Density | 10% | 8 | 8 × 0.10 | 0.80 |
| Threat Density | 10% | 7 | 7 × 0.10 | 0.70 |
| Resilience | 5% | 6 | 6 × 0.05 | 0.30 |
| **TOTAL** | **100%** | | | **7.30** |

**Quantitative Base Score**: 7.3/10

This indicates a **Power 7** deck leaning toward **Power 8** (High Power tier).

---

## Quick Reference Tables

### Power Level by Average Win Turn

| Win Turn | Power Level |
|----------|-------------|
| 2-3 | 10 |
| 4 | 9 |
| 5-6 | 8 |
| 7-8 | 7 |
| 9-10 | 6 |
| 11-12 | 5 |
| 13-14 | 4 |
| 15-16 | 3 |
| 17-18 | 2 |
| 19+ | 1 |

### Power Level by Fast Mana Count

| Fast Mana Pieces | Power Level |
|------------------|-------------|
| 8+ | 10 |
| 6-7 | 9 |
| 5 | 8 |
| 4 | 7 |
| 3 | 6 |
| 2 | 5 |
| 1 + inefficient | 4 |
| 1 (Sol Ring) | 2-3 |
| 0 | 1 |

### Power Level by Synergy Density

| Tier 1-2 % | Power Level |
|-----------|-------------|
| 90%+ | 10 |
| 80-89% | 9 |
| 70-79% | 8 |
| 60-69% | 7 |
| 50-59% | 6 |
| 40-49% | 5 |
| 30-39% | 4 |
| 20-29% | 3 |
| 10-19% | 2 |
| <10% | 1 |

### Power Level by Interaction Count

| Interaction Pieces | Power Level |
|-------------------|-------------|
| 15+ | 10 |
| 12-14 | 9 |
| 10-12 | 8 |
| 9-10 | 7 |
| 7-8 | 6 |
| 6-7 | 5 |
| 4-5 | 4 |
| 3 | 3 |
| 1-2 | 2 |
| 0-1 | 1 |

---

## Common Scoring Scenarios

### Scenario 1: High-Power cEDH Deck

- Speed: 9 (turn 4 wins)
- Mana Base: 9 (fetches, duals, 32 lands)
- Fast Mana: 9 (7 pieces including Crypt, Vault, signets)
- Card Draw: 9 (13 sources, 6 tutors)
- Interaction: 9 (14 pieces, free spells, instant speed)
- Synergy: 9 (85% Tier 1-2)
- Threats: 9 (4 compact combos, high redundancy)
- Resilience: 8 (strong protection, good recursion)

**Weighted Score**: (9×0.2) + (9×0.15) + (9×0.1) + (9×0.15) + (9×0.15) + (9×0.1) + (9×0.1) + (8×0.05) = **8.95 → 9**

**Rating**: Power 9 (Fringe cEDH)

### Scenario 2: Optimized Casual Deck

- Speed: 6 (turn 9-10 wins)
- Mana Base: 6 (37 lands, 45% Tier 1-2)
- Fast Mana: 6 (3 pieces: Sol Ring, Arcane Signet, 1 talisman)
- Card Draw: 6 (8 sources, 2 tutors)
- Interaction: 6 (8 pieces, mix of speeds)
- Synergy: 6 (55% Tier 1-2)
- Threats: 6 (2 win conditions, some redundancy)
- Resilience: 5 (basic protection, minimal recursion)

**Weighted Score**: (6×0.2) + (6×0.15) + (6×0.1) + (6×0.15) + (6×0.15) + (6×0.1) + (6×0.1) + (5×0.05) = **5.95 → 6**

**Rating**: Power 6 (Focused/Optimized Casual)

### Scenario 3: Upgraded Precon

- Speed: 4 (turn 13-14 wins)
- Mana Base: 4 (38 lands, 25% Tier 1-2)
- Fast Mana: 4 (Sol Ring + inefficient ramp)
- Card Draw: 4 (5 sources, 0 tutors)
- Interaction: 4 (5 pieces, expensive)
- Synergy: 4 (35% Tier 1-2)
- Threats: 4 (1 primary + weak backup)
- Resilience: 3 (minimal protection)

**Weighted Score**: (4×0.2) + (4×0.15) + (4×0.1) + (4×0.15) + (4×0.15) + (4×0.1) + (4×0.1) + (3×0.05) = **3.95 → 4**

**Rating**: Power 4 (Casual/Upgraded Precon)

---

## Notes

### Rounding Guidelines

- If the weighted score ends in .0-.2, round down (e.g., 7.2 → 7)
- If the weighted score ends in .3-.7, consider context (e.g., 7.5 could be 7 or 8)
- If the weighted score ends in .8-.9, round up (e.g., 7.8 → 8)

**Context considerations**:
- If the deck "feels" like the higher tier based on tier definitions, round up
- If the deck has significant weaknesses not captured in metrics, round down
- When in doubt, use half-points (e.g., 7.5)

### Metric Weight Rationale

**Why Speed is 20%**: Speed is the most universal indicator of power level across all archetypes.

**Why Mana Base/Fast Mana are separate**: Mana base quality affects consistency; fast mana affects explosive starts. Both matter but differently.

**Why Draw and Interaction are 15% each**: Both are critical for executing strategy and staying in the game.

**Why Resilience is only 5%**: Resilience matters less if the deck can win quickly or through disruption. It's a modifier, not a core metric.

---

## Conclusion

This scoring calculator provides objective frameworks for converting observations into numerical scores. Use these tables alongside the full rubric to produce consistent, defensible power level ratings.

For more guidance, see:
- [RUBRIC.md](RUBRIC.md) - Complete evaluation framework
- [EVALUATION_TEMPLATE.md](EVALUATION_TEMPLATE.md) - Blank evaluation worksheet
- [REFERENCE_DECKS.md](REFERENCE_DECKS.md) - Example evaluations
- [FAQ.md](FAQ.md) - Common questions and edge cases
