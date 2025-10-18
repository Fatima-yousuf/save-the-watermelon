# src/logic.py

def check_guess(secret_word, guessed_letters, guess):
    """
    Checks if the guessed letter is in the secret word.
    Returns True if correct, False otherwise.
    """
    if guess in guessed_letters:
        return None  # Already guessed
    guessed_letters.add(guess)
    return guess in secret_word

def is_word_revealed(secret_word, guessed_letters):
    """
    Returns True if all letters in the secret word have been guessed.
    """
    return all(letter in guessed_letters for letter in secret_word)

def get_masked_word(secret_word, guessed_letters):
    """
    Returns the secret word with unguessed letters masked as underscores.
    """
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
