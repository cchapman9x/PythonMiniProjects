# PythonMiniProjects

PythonMiniProjects is a collection of small Python projects, experiments, and reusable code snippets that I’m building to review what I know, rebuild my programming skills, and explore new concepts. It serves as both a project bank and a snippet bank. It is a place to practice problem-solving, investigate how code behaves, and build small programs independently.

Each project begins with a simple, usable version that I may revisit as my skills develop. The project bank provides ideas to choose from, rather than a required sequence or a list of completed work. Snippets capture focused examples and approaches that I can reference or reuse in future projects.

Nenomorph tools, engineering projects, reusable engineering libraries, and larger applications belong in separate repositories. If an experiment here grows into a standalone tool such as a GUI calculator or converter, then it may move into its own dedicated repository for continued development.

#### Organization
- <b>Mini Projects</b>
- <b>Snippets & Tests</b>

<hr>

### Project Tracking
Each project has two checkboxes:
- <b>Built</b>: A working version is finished
- <b>Uploaded</b>: That version has been added to this repository

Change `[ ]` to `[x]` as each milestone is reached. All projects currently remain unchecked in this tracker.

<hr>

### Learning Levels
| Level | Typical concepts |
| --- | --- |
| Starter (S) | Input, variables, arithmetic, conditions, loops, and small collections. |
| Intermediate (I) | Multiple functions, file handling, or more involved program state. |
| Advanced (A) | Additional mathematics, algorithms, or simulation concepts. |

These labels describe rough prerequisites. Individual projects may use only some of the listed concepts.

<hr>

### Mini Project Bank
These are optional practice ideas, not a required order or a list of completed work. Some involve concepts I will learn in later sections of the course. Additional snippet experiments can be added as I go.

**40 optional ideas · Updated October 10, 2026**

- [Everyday Scripts](#everyday-scripts)
- [Text Challenges](#text-challenges)
- [Collections and Data](#collections-and-data)
- [File and Format Experiments](#file-and-format-experiments)
- [Number and Randomness Experiments](#number-and-randomness-experiments)
- [Small Terminal Games](#small-terminal-games)

#### Everyday Scripts

<details>
<summary>View 6 project ideas</summary>
  
##### Bill Splitter

**Level:** Basics

**Purpose:** Estimate each person’s share of a bill.

**Small version:** Accept a bill total, tip percentage, and positive party size; print the total and per-person estimate rounded to two decimal places.

**Resources:** [S01](https://docs.python.org/3/library/decimal.html)

- [ ] Built
- [ ] Uploaded

---

##### Recipe Batch Scaler

**Level:** Basics

**Purpose:** Adjust a few ingredient quantities for a different serving count.

**Small version:** Accept original and desired servings plus ingredient amounts; apply the same scale factor and preserve units. Keep everything in one terminal session.

**Resources:** [S13](https://docs.python.org/3/library/fractions.html)

- [ ] Built
- [ ] Uploaded

---

#### Countdown Timer

**Level:** Next

**Purpose:** Practice a loop that updates over time.

**Small version:** Accept a short duration in seconds, display the remaining time, and announce completion. Use the standard library; keep the first version to one countdown.

- [ ] Built
- [ ] Uploaded

---

#### Date Gap Checker

**Level:** Next

**Purpose:** Find the number of days between two calendar dates.

**Small version:** Accept dates in one documented format, reject invalid dates, and report the signed day difference. Include an example crossing a month or leap-year boundary.

**Resources:** [S03](https://docs.python.org/3/library/datetime.html)

- [ ] Built
- [ ] Uploaded

---

#### Study Log Summary

**Level:** Next

**Purpose:** Summarize a small set of recorded study sessions.

**Small version:** Use a supplied list of subject/minute pairs; total time by subject and overall, and report the longest session. Keep it as a one-run summary script.

**Resources:** [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Random Task Picker

**Level:** Basics

**Purpose:** Choose a practice task from a short list.

**Small version:** Accept a handful of task names, reject an empty list, and select one at random. Add an option to draw several distinct tasks if desired.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

### Text Challenges

#### Text Statistics

**Level:** Basics

**Purpose:** Summarize a passage of text.

**Small version:** Count characters and words, then report repeated words. State how punctuation and letter case are handled, and handle empty input.

**Resources:** [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Word Puzzle Finder

**Level:** Next

**Purpose:** Find words that can be made from supplied letters.

**Small version:** Search a small provided word list and ensure each match uses no more copies of a letter than are available. Return unique matches.

**Resources:** [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Bracket Balance Checker

**Level:** Next

**Purpose:** Locate mismatched brackets in plain text.

**Small version:** Track parentheses, square brackets, and braces; report the position of a mismatch or an unclosed bracket. Do not attempt to parse programming-language strings or comments.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### ISBN-13 Check

**Level:** Next

**Purpose:** Catch format and check-digit errors in an ISBN-13.

**Small version:** Normalize spaces and hyphens, check length and prefix, and calculate the check digit. Report structural validity without claiming the number belongs to a published book.

**Resources:** [S08](https://www.isbn-international.org/sites/default/files/ISBN%20Manual%202012%20-corr.pdf)

- [ ] Built
- [ ] Uploaded

---

#### Run-Length Encoding Experiment

**Level:** Next

**Purpose:** Explore reversible encoding of consecutive repeated characters.

**Small version:** Encode text as a list of count/character pairs, decode it, and verify an exact round trip. Include digits, spaces, and empty text.

**Resources:** [S10](https://docs.python.org/3/library/itertools.html#itertools.groupby)

- [ ] Built
- [ ] Uploaded

---

#### Palindrome Checker

**Level:** Basics

**Purpose:** Check whether text reads the same forward and backward.

**Small version:** Compare both a literal version and a version normalized for case and non-alphanumeric characters. Show which interpretation produced the result.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Caesar Cipher Experiment

**Level:** Basics

**Purpose:** Practice shifting letters while preserving other characters.

**Small version:** Accept text and an integer shift, wrap around the alphabet, and reverse the shift to decode. Treat this as a word puzzle, not secure encryption.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Word Wrap Experiment

**Level:** Next

**Purpose:** Break a paragraph into lines of a chosen width.

**Small version:** Build lines word by word, preserve whole words, and explain how words longer than the requested width are handled. Compare a few widths.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

### Collections and Data

#### Duplicate Finder

**Level:** Basics

**Purpose:** Identify repeated entries in a collection.

**Small version:** Accept a list of names or labels, report duplicate counts, and produce a deduplicated list that preserves first appearance.

**Resources:** [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### List Comparison

**Level:** Basics

**Purpose:** Compare two collections of labels.

**Small version:** Show shared values and values unique to each collection using sets. State that this comparison ignores repetition and display results in a predictable order.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Vote Counter

**Level:** Basics

**Purpose:** Count choices in a small sample poll.

**Small version:** Tally a supplied list of votes, show totals, and identify all tied leaders. Decide how empty or unrecognized choices are handled.

**Resources:** [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Leaderboard Sorter

**Level:** Next

**Purpose:** Practice sorting structured records.

**Small version:** Use a short list of player/score records; sort highest score first and break ties alphabetically. Display the ordered results.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Tag Overlap Finder

**Level:** Basics

**Purpose:** Find entries that share selected tags.

**Small version:** Give a few sample items sets of tags, accept a query set, and report how many query tags match each item. Keep the dataset small and in memory.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Nested Dictionary Lookup

**Level:** Next

**Purpose:** Retrieve a value inside a nested record.

**Small version:** Accept a dotted key path such as profile.settings.theme, walk a sample dictionary, and distinguish a missing key from a stored None value.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Shopping Cart Receipt

**Level:** Basics

**Purpose:** Turn a few item records into a readable receipt.

**Small version:** Store item names, quantities, and unit prices; calculate line totals and a grand total. Use integer cents if exact money totals are required.

**Resources:** [S01](https://docs.python.org/3/library/decimal.html)

- [ ] Built
- [ ] Uploaded

---

#### Duplicate Record Merger

**Level:** Next

**Purpose:** Combine repeated records using a documented rule.

**Small version:** Use sample records with IDs; merge matching IDs while preserving unrelated records. Define whether newer values replace older ones and report conflicts.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

### File and Format Experiments

#### Text File Difference

**Level:** Next

**Purpose:** Show which lines differ between two small files.

**Small version:** Read both files, compare corresponding lines with line numbers, and report extra lines when one file is longer. Keep the comparison position-based.

**Resources:** [S35](https://docs.python.org/3/library/pathlib.html)

- [ ] Built
- [ ] Uploaded

---

#### CSV Summary

**Level:** Next

**Purpose:** Practice reading structured rows from a file.

**Small version:** Read a tiny CSV of labels and numbers, summarize valid rows, and report missing or malformed values. Print a summary without modifying the input.

**Resources:** [S02](https://docs.python.org/3/library/csv.html)

- [ ] Built
- [ ] Uploaded

---

#### JSON Save and Load

**Level:** Next

**Purpose:** Practice saving and restoring a small collection.

**Small version:** Write a few simple records to a new JSON file, load them again, and compare the result with the original. Handle missing or invalid files.

- [ ] Built
- [ ] Uploaded

---

#### Folder Extension Count

**Level:** Next

**Purpose:** Inspect the kinds of files in a selected folder.

**Small version:** Count regular files by suffix and include a no-extension category. Start with one directory, document case handling, and keep the scan read-only.

**Resources:** [S35](https://docs.python.org/3/library/pathlib.html)

- [ ] Built
- [ ] Uploaded

---

#### Log Level Counter

**Level:** Next

**Purpose:** Summarize a small sample log.

**Small version:** Read a provided text log with a documented format, count INFO/WARNING/ERROR entries, and report unrecognized lines rather than silently losing them.

**Resources:** [S05](https://docs.python.org/3/library/re.html), [S35](https://docs.python.org/3/library/pathlib.html)

- [ ] Built
- [ ] Uploaded

---

#### Markdown Link Extractor

**Level:** Next

**Purpose:** Find simple inline links in a Markdown sample.

**Small version:** Extract labels and URLs, remove duplicate URLs, and display a list. Limit the first version to simple inline links; document unsupported Markdown forms.

**Resources:** [S05](https://docs.python.org/3/library/re.html)

- [ ] Built
- [ ] Uploaded

---

### Number and Randomness Experiments

#### Collatz Sequence

**Level:** Basics

**Purpose:** Explore an integer sequence using loops and conditions.

**Small version:** Accept a positive integer, halve even values and transform odd values to 3n+1; show steps and peak value. Stop at 1 or a chosen step limit.

**Resources:** [S16](https://mathworld.wolfram.com/CollatzConjecture.html)

- [ ] Built
- [ ] Uploaded

---

#### Dice Roll Distribution

**Level:** Basics

**Purpose:** See how simulated roll frequencies compare.

**Small version:** Roll a six-sided die a chosen number of times, count each outcome, and print counts and percentages. Allow a fixed random seed for repeatable runs.

**Resources:** [S29](https://docs.python.org/3/library/random.html), [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Coin Toss Streaks

**Level:** Basics

**Purpose:** Track consecutive outcomes in a sequence.

**Small version:** Simulate a chosen number of tosses and report totals plus the longest heads and tails streaks. Check the logic on a short hand-written sequence first.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

#### One-Dimensional Random Walk

**Level:** Basics

**Purpose:** Explore a simple sequence of left/right steps.

**Small version:** Start at zero, randomly add or subtract one per step, and record the path, final position, and furthest distance reached. Print a compact summary.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

#### Birthday Match Experiment

**Level:** Next

**Purpose:** Estimate how often a group contains matching birthdays.

**Small version:** Simulate many groups and count those with at least one shared birthday. Assume 365 equally likely days and no leap days; print the fraction of matching groups.

**Resources:** [S29](https://docs.python.org/3/library/random.html), [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Random Drawing Without Replacement

**Level:** Basics

**Purpose:** Practice selecting distinct entries.

**Small version:** Draw a chosen number of names or numbered tickets, ensure no entry is selected twice, and handle a request larger than the available pool.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

### Small Terminal Games

#### Tic-Tac-Toe

**Level:** Next

**Purpose:** Build a complete two-player terminal game.

**Small version:** Display a board, alternate turns, reject invalid moves, and detect wins or draws. Keep the first version to two human players.

**Resources:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Built
- [ ] Uploaded

---

#### Hangman

**Level:** Next

**Purpose:** Build a word-guessing game.

**Small version:** Choose from a small local word list, reveal correct letters, track incorrect and repeated guesses, and end when the word is solved or the guess limit is reached.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

#### Blackjack

**Level:** Next

**Purpose:** Practice state and decisions in a simplified card game.

**Small version:** Deal from a standard deck, support hit/stand and flexible ace values, and detect wins, losses, and ties. State the dealer rule; omit betting and splitting.

**Resources:** [S29](https://docs.python.org/3/library/random.html), [S30](https://bicyclecards.com/how-to-play/blackjack/)

- [ ] Built
- [ ] Uploaded

---

#### Poker Hand Classifier

**Level:** Next

**Purpose:** Classify a five-card hand.

**Small version:** Accept five distinct cards, identify the category, and handle an ace-low straight. Keep the scope to classification rather than a complete poker game.

**Resources:** [S32](https://bicyclecards.com/how-to-play/basics-of-poker)

- [ ] Built
- [ ] Uploaded

---

#### Mastermind-Style Code Guessing

**Level:** Next

**Purpose:** Build a short deduction game.

**Small version:** Generate a hidden sequence of symbols, accept guesses, and report exact-position and wrong-position matches without double-counting repeated symbols. Set a guess limit.

**Resources:** [S29](https://docs.python.org/3/library/random.html), [S06](https://docs.python.org/3/library/collections.html)

- [ ] Built
- [ ] Uploaded

---

#### Rock-Paper-Scissors Match

**Level:** Basics

**Purpose:** Practice input checking, conditions, and score tracking.

**Small version:** Play a chosen number of rounds against random computer choices, report each outcome, and display the final score. Re-prompt after invalid choices.

**Resources:** [S29](https://docs.python.org/3/library/random.html)

- [ ] Built
- [ ] Uploaded

---

## Snippet Bank

**12 focused experiments.** Each snippet should answer a specific question about Python, show its inputs and output, and include a short explanation. These are separate from the mini projects above.

#### List changes and return values

Compare append, insert, remove, and pop; record both the resulting list and each method’s return value.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Aliasing and copying

Compare assignment, a shallow copy, and a deep copy of a nested list; observe which edits affect the original.

- [ ] Tested and understood
- [ ] Uploaded

---

#### Sorting in place versus making a copy

Compare list.sort() with sorted(), including return values and the order of the original list.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### None versus other false-like values

Compare None, zero, False, and an empty string; practice is None separately from truth-value checks.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Type hints at runtime

Annotate a variable, reassign a different type, and compare Python’s runtime behavior with any editor diagnostic.

- [ ] Tested and understood
- [ ] Uploaded

---

#### Missing dictionary keys

Compare indexing, get(), and membership checks; distinguish a missing key from a key whose value is None.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Tuple containing a mutable item

Compare attempts to replace a tuple item with edits to a list stored inside that tuple.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Set operations

Compare union, intersection, difference, and symmetric difference using two small collections with overlap.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Identity versus equality

Compare two equal lists with two names pointing to the same list; record the results of == and is.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Slicing boundaries

Try omitted bounds, negative indices, and step values; record expected and actual slices of the same sequence.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Input conversion failures

Try converting whole-number, decimal, blank, and nonnumeric strings; record what succeeds and what exception occurs.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

#### Tuple unpacking

Compare ordinary and starred unpacking, including too few or too many values; capture the resulting variables or errors.

**Resource:** [S07](https://docs.python.org/3/library/stdtypes.html)

- [ ] Tested and understood
- [ ] Uploaded

---

## Resources

All 35 links from the original project bank are retained below, grouped by purpose. The original bank records them as consulted on October 3, 2026. The Python references support practice scripts and snippets; the broader references remain available for background reading and future work in other repositories.

A reference explains a language feature, formula, format, or game rule. It is not a requirement to build a full tool or follow a complete course.

### Python Language and Standard Library

| ID   | Resource                                                     |
| ---- | ------------------------------------------------------------ |
| S01  | [Python documentation - exact decimal arithmetic and rounding](https://docs.python.org/3/library/decimal.html) |
| S02  | [Python documentation - CSV reading and writing](https://docs.python.org/3/library/csv.html) |
| S03  | [Python documentation - dates and date arithmetic](https://docs.python.org/3/library/datetime.html) |
| S04  | [Python documentation - calendar operations](https://docs.python.org/3/library/calendar.html) |
| S05  | [Python documentation - text patterns and regular expressions](https://docs.python.org/3/library/re.html) |
| S06  | [Python documentation - counting collections and queues](https://docs.python.org/3/library/collections.html) |
| S07  | [Python documentation - integer representations and bit operations](https://docs.python.org/3/library/stdtypes.html) |
| S10  | [Python documentation - grouping consecutive values](https://docs.python.org/3/library/itertools.html#itertools.groupby) |
| S11  | [Python documentation - square roots, distances, and numeric comparisons](https://docs.python.org/3/library/math.html) |
| S13  | [Python documentation - exact fractions and normalized representation](https://docs.python.org/3/library/fractions.html) |
| S14  | [Python documentation - descriptive statistics and sample deviation](https://docs.python.org/3/library/statistics.html) |
| S29  | [Python documentation - random selection, sampling, and shuffling](https://docs.python.org/3/library/random.html) |
| S35  | [Python documentation - reading files and traversing paths](https://docs.python.org/3/library/pathlib.html) |

### Text Formats and Games

| ID   | Resource                                                     |
| ---- | ------------------------------------------------------------ |
| S08  | [International ISBN Agency - ISBN structure and check-digit calculation](https://www.isbn-international.org/sites/default/files/ISBN%20Manual%202012%20-corr.pdf) |
| S09  | [Rosetta Code - Roman numeral decoding task](https://rosettacode.org/wiki/Roman_numerals/Decode) |
| S30  | [Bicycle Playing Cards - Blackjack rules](https://bicyclecards.com/how-to-play/blackjack/) |
| S31  | [Scholarpedia - Conway's Game of Life](https://www.scholarpedia.org/article/Game_of_Life) |
| S32  | [Bicycle Playing Cards - five-card poker hand rankings](https://bicyclecards.com/how-to-play/basics-of-poker) |
| S33  | [United States Bowling Congress - scoring and bonus rolls](https://bowl.com/keeping-score) |

### Math, Algorithms, and Broader Engineering References

| ID   | Resource                                                     |
| ---- | ------------------------------------------------------------ |
| S12  | [OpenStax - primes, factors, and divisibility](https://openstax.org/books/contemporary-mathematics/pages/3-1-prime-and-composite-numbers) |
| S15  | [NumPy documentation - matrix multiplication and compatible dimensions](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) |
| S16  | [Wolfram MathWorld - Collatz sequence and conjecture](https://mathworld.wolfram.com/CollatzConjecture.html) |
| S17  | [OpenStax Calculus Volume 2 - numerical integration](https://openstax.org/books/calculus-volume-2/pages/3-6-numerical-integration) |
| S18  | [OpenStax Calculus Volume 2 - Taylor and Maclaurin series](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series) |
| S19  | [DigiKey - resistor color bands, multipliers, and tolerances](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code) |
| S20  | [OpenStax College Physics 2e - Ohm's law](https://openstax.org/books/college-physics-2e/pages/20-2-ohms-law-resistance-and-simple-circuits) |
| S21  | [OpenStax College Physics 2e - series and parallel resistance](https://openstax.org/books/college-physics-2e/pages/21-1-resistors-in-series-and-parallel) |
| S22  | [DigiKey - voltage divider calculation](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-voltage-divider) |
| S23  | [Adafruit - LED series-resistor calculations](https://learn.adafruit.com/lets-put-leds-in-things/from-scratch) |
| S24  | [OpenStax Contemporary Mathematics - truth tables](https://openstax.org/books/contemporary-mathematics/pages/2-3-constructing-truth-tables) |
| S25  | [OpenStax College Physics 2e - vector components and resultants](https://openstax.org/books/college-physics-2e/pages/3-3-vector-addition-and-subtraction-analytical-methods) |
| S26  | [OpenStax College Physics 2e - constant-acceleration motion](https://openstax.org/books/college-physics-2e/pages/2-5-motion-equations-for-constant-acceleration-in-one-dimension) |
| S27  | [OpenStax College Physics 2e - projectile motion](https://openstax.org/books/college-physics-2e/pages/3-4-projectile-motion) |
| S28  | [Princeton Algorithms - shortest paths using breadth-first search](https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/BreadthFirstPaths.html) |
| S34  | [NIST - International System of Units reference](https://physics.nist.gov/cuu/Reference/contents.html) |

<hr>

### License
MIT License. See the repository's LICENSE file for the full terms
