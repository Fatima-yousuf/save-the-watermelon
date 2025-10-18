import unittest
from src.logic import check_guess, is_word_revealed, get_masked_word

class TestLogic(unittest.TestCase):

    def test_check_guess_correct(self):
        guessed = set()
        result = check_guess("apple", guessed, "a")
        self.assertTrue(result)
        self.assertIn("a", guessed)

    def test_check_guess_incorrect(self):
        guessed = set()
        result = check_guess("apple", guessed, "z")
        self.assertFalse(result)
        self.assertIn("z", guessed)

    def test_check_guess_repeat(self):
        guessed = {"a"}
        result = check_guess("apple", guessed, "a")
        self.assertIsNone(result)

    def test_is_word_revealed_true(self):
        guessed = set("apple")
        self.assertTrue(is_word_revealed("apple", guessed))

    def test_is_word_revealed_false(self):
        guessed = {"a", "p"}
        self.assertFalse(is_word_revealed("apple", guessed))

    def test_get_masked_word(self):
        guessed = {"a", "p"}
        masked = get_masked_word("apple", guessed)
        self.assertEqual(masked, "a p p _ _")

if __name__ == "__main__":
    unittest.main()

