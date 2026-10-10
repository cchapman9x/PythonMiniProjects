# PythonMiniProjects

PythonMiniProjects is a collection of small Python projects, experiments, and reusable code snippets that I’m building to review what I know, rebuild my programming skills, and explore new concepts. It serves as both a project bank and a snippet bank. It is a place to practice problem-solving, investigate how code behaves, and build small programs independently.

Each project begins with a simple, usable version that I may revisit as my skills develop. The project bank provides ideas to choose from, rather than a required sequence or a list of completed work. Snippets capture focused examples and approaches that I can reference or reuse in future projects.

Nenomorph tools, engineering projects, reusable engineering libraries, and larger applications belong in separate repositories. If an experiment here grows into a standalone tool such as a GUI calculator or converter, then it may move into its own dedicated repository for continued development.

#### Organization
- Mini Projects: Give each project its own folder with its code and a brief explanation of what it does and how to run it.
- Snippets & Tests: Group related experiments by topic. Use comments to explain the question being tested and the observed result.

<hr>

### Project Tracking
Each project has two checkboxes:
- Built: A working version is finished
- Uploaded: That version has been added to this repository

Change [ ] to [x] as each milestone is reached. All projects currently remain unchecked in this tracker.

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
- Built: The small working version is finished.
- Uploaded: That version has been added to this repository.

Small Everyday Scripts
<details>
<summary>View 2 ideas</summary>

Bill Splitter
Accept a bill total, tip percentage, and number of people, then calculate the amount each person owes. Practice numeric input, arithmetic, and formatted output. Keep the result as an estimate rounded to two decimal places.
- [ ] Built
- [ ] Uploaded
Recipe Batch Scaler
Enter the original and desired serving counts and a few ingredient quantities. Print the scaled quantities while keeping their units. Practice arithmetic and collections in a single terminal session.
- [ ] Built
- [ ] Uploaded
</details>

Text and Collection Challenges
<details>
<summary>View 6 ideas</summary>

Text Statistics
Accept a passage of text and report character and word counts, then count repeated words. Practice strings and dictionaries; define how punctuation and letter case are handled.
- [ ] Built
- [ ] Uploaded
Word Puzzle Finder
Use a small supplied word list to find words that can be formed from entered letters. Track repeated letters correctly. Practice loops, collections, and counting.
- [ ] Built
- [ ] Uploaded
Bracket Balance Checker
Check whether parentheses, brackets, and braces are balanced in a short string, and report a mismatch. Treat the input as plain text rather than attempting to parse Python code.
- [ ] Built
- [ ] Uploaded
ISBN-13 Check
Remove spaces and hyphens from an entered ISBN-13, then check its format and check digit. Practice string processing, arithmetic, and validation. This checks the number’s structure, not whether a book exists.
- [ ] Built
- [ ] Uploaded
Run-Length Encoding Experiment
Encode repeated characters as count/character pairs and decode them back to the original text. Use a list of pairs so digits in the text are unambiguous. Practice iteration and verify that decoding reproduces the input.
- [ ] Built
- [ ] Uploaded
Collatz Sequence
Start with a positive integer and generate its Collatz sequence. Show the sequence, number of steps, and largest value reached. Stop at 1 or a chosen step limit. Practice loops and conditions.
- [ ] Built
- [ ] Uploaded
</details>

Small Terminal Games
<details>
<summary>View 4 ideas</summary>

Tic-Tac-Toe
Build a two-player terminal game with a board, alternating turns, valid-move checks, and win/draw detection. Keep the first version to two human players.
- [ ] Built
- [ ] Uploaded
Hangman
Choose a word from a small local list, reveal correctly guessed letters, and track incorrect or repeated guesses. End the round when the word is solved or the guess limit is reached.
- [ ] Built
- [ ] Uploaded
Blackjack
Build a simplified player-versus-dealer round with hit/stand, flexible ace values, and win/loss/tie results. State the dealer rule and leave out betting, splitting, accounts, and other app features.
- [ ] Built
- [ ] Uploaded
Poker Hand Classifier
Accept five distinct cards and identify the hand category, including an ace-low straight. Keep this as a classification exercise rather than a complete poker game.
- [ ] Built
- [ ] Uploaded
</details>

<hr>

### License
MIT License. See the repository's LICENSE file for the full terms
