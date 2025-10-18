# Save the Watermelon - Pseudocode

FUNCTION main_game_loop
  secret_word ← get_random_word()
  guessed_letters ← empty set
  slices ← 5  # or any default number

  WHILE slices > 0 AND NOT is_word_revealed(secret_word, guessed_letters)
    DISPLAY get_masked_word(secret_word, guessed_letters)
    guess ← prompt_for_letter()
    IF guess in guessed_letters THEN
      DISPLAY "You already guessed that letter!"
      CONTINUE
    ENDIF
    ADD guess TO guessed_letters
    IF guess IN secret_word THEN
      DISPLAY "Correct!"
    ELSE
      slices ← slices - 1
      DISPLAY "Incorrect! Slices remaining: " + slices
    ENDIF
  ENDWHILE

  IF is_word_revealed(secret_word, guessed_letters) THEN
    DISPLAY "You saved the watermelon!"
  ELSE
    DISPLAY "Oh no! The watermelon was sliced!"
  ENDIF
END FUNCTION
