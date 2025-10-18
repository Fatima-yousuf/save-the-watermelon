# Save the Watermelon - Test Plan

## Game Testing Overview
This document shows how the game was tested to ensure it works correctly.

## Test Cases

| Test Case       | Input            | Expected Result                          | Actual Result                         | Pass/Fail |
|-----------------|-----------------|----------------------------------------|--------------------------------------|-----------|
| Correct guess   | Letter in word  | Letter revealed in masked word          | Letter revealed in masked word        | Pass      |
| Incorrect guess | Letter not in word | Slice count decreases                  | Slice count decreased by 1            | Pass      |
| Repeat guess    | Letter already guessed | Message "Already guessed"           | Message "Already guessed"             | Pass      |
| Non-letter input| Number or symbol | Error message, input rejected           | Input rejected, error shown           | Pass      |
| Win scenario    | Guess all letters| Message "You saved the watermelon!"    | Message displayed correctly           | Pass      |
| Lose scenario   | Run out of slices| Message "Oh no! The watermelon was sliced!" | Message displayed correctly    | Pass      |

## Screenshots
- Win screenshot: `docs/screenshots/win.png`  
- Lose screenshot: `docs/screenshots/lose.png`
