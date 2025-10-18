# src/game.py
from .logic import check_guess, is_word_revealed, get_masked_word
from .words import get_random_word

def main():
    secret_word = get_random_word()
    guessed_letters = set()
    slices = 5  # number of wrong guesses allowed

    print("Welcome to Save the Watermelon!")
    
    while slices > 0 and not is_word_revealed(secret_word, guessed_letters):
        print("\nWord:", get_masked_word(secret_word, guessed_letters))
        print(f"Slices remaining: {slices}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        result = check_guess(secret_word, guessed_letters, guess)
        if result is None:
            print("You already guessed that letter!")
        elif result:
            print("Nice guess!")
        else:
            slices -= 1
            print(f"Sliced! Remaining slices: {slices}")

    if is_word_revealed(secret_word, guessed_letters):
        print(f"You saved the watermelon! The word was '{secret_word}'.")
    else:
        print(f"Oh no! The watermelon was sliced. The word was '{secret_word}'.")

if __name__ == "__main__":
    main()
