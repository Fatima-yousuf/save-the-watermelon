# Save the Watermelon - Test Plan

## Game Testing Overview
This document shows how the game was tested to ensure it works correctly.

## Test Cases

| Test Case | Input | Expected Result | Actual Result | Pass/Fail |
|-----------|-------|----------------|---------------|-----------|
| Correct guess | Letter in word | Letter revealed in masked word | | |
| Incorrect guess | Letter not in word | Slice count decreases | | |
| Repeat guess | Letter already guessed | Message "Already guessed" | | |
| Non-letter input | Number or symbol | Error message, input rejected | | |
| Win scenario | Guess all letters | Message "You saved the watermelon!" | | |
| Lose scenario | Run out of slices | Message "Oh no! The watermelon was sliced!" | | |

## Screenshots
- Win screenshot: `docs/screenshots/win.png`  
- Lose screenshot: `docs/screenshots/lose.png`
