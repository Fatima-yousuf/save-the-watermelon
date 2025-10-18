# Save the Watermelon - Design

## Problem Statement & Target Audience
Players want a fun, simple word-guessing game where they can try to save a watermelon before it gets sliced. The target audience includes beginners learning Python games, kids, and casual players.

## Game Rules & Win/Lose Conditions
- A random secret word is selected.
- Player guesses one letter at a time.
- Correct guesses reveal the letter in the word.
- Incorrect guesses reduce the slice counter (number of lives).
- Player wins if all letters are revealed before slices run out.
- Player loses if slices reach 0 before guessing the word.

## Core Features (Must-Have)
- Random word selection
- Masked word display (underscores for unguessed letters)
- Track guessed letters
- Slice counter for lives
- Win/lose detection

## Stretch Goals (Nice-to-Have)
- ASCII art stages for the watermelon
- Difficulty levels (word length, slice count)
- Word categories
- Scoreboard and streaks

## Flow (Basic)
1. Start game
2. Select random word
3. Initialize slices and guessed letters
4. Loop:
   - Display masked word
   - Prompt player for a guess
   - Validate input
   - Update guessed letters
   - Reduce slices if wrong
   - Check win/lose
5. End game (win/lose)
6. Option to replay

## Data Design
- `secret_word` → string of chosen word
- `guessed_letters` → set of letters guessed by player
- `slices` → integer for remaining lives

## Module / Function Responsibilities
- `words.py` → word list and random selection
- `logic.py` → check_guess, is_word_revealed, get_masked_word
- `game.py` → main game loop, input/output, replay option
