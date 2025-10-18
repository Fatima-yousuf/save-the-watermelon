# Save the Watermelon 🍉

## Project Description
Save the Watermelon is a terminal-based word-guessing game built in Python. Players must guess letters to reveal a secret word before the "slice counter" runs out. If the counter reaches 0, the watermelon is sliced! The game helps practice Python fundamentals, input validation, and modular code design.

## Features & Rules
- Randomly selects a secret word from a predefined list.
- Shows a masked version of the word (e.g., `_ a _ e`).
- Players guess letters one at a time.
- Correct guesses reveal letters.
- Incorrect guesses reduce the number of slices (lives).
- Win if all letters are revealed before slices run out.
- Lose if slices reach 0.

### Optional Features (Stretch Goals)
- ASCII art for the watermelon stages
- Difficulty levels (word length, slice count)
- Word categories
- Session scoreboard

## How to Run the Game
Open your terminal, navigate to the project folder, and run:

```bash
cd ~/save-the-watermelon
python3 src/game.py
```
## How to Test the Game

### Use the following test cases to verify that the game works correctly:

| Test Case       | Input                  | Expected Result                          |
|-----------------|----------------------|-----------------------------------------|
| Correct guess    | Letter in word        | Letter revealed in masked word          |
| Incorrect guess  | Letter not in word    | Slice count decreases                    |
| Repeat guess     | Letter already guessed| Message "Already guessed"               |
| Non-letter input | Number or symbol      | Error message, input rejected           |
| Win scenario     | Guess all letters     | Message "You saved the watermelon!"     |
| Lose scenario    | Run out of slices     | Message "Oh no! The watermelon was sliced!" |

### Automated Testing (Optional)
If you want to run the built-in unit tests, run this command in your terminal:

```bash
python3 -m unittest discover -s tests
```
## Screenshots
### Win
![Win Screenshot 1](docs/screenshots/Win%20Screenshot-docs.png)
![Win Screenshot 2](docs/screenshots/Win-Screenshot-docs-.png)

### Lose
![Lose Screenshot 1](docs/screenshots/Lose%20Screenshot-docs.png)
![Lose Screenshot 2](docs/screenshots/Lose-Screenshot-docs-.png)
