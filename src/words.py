# src/words.py
import random

WORD_LIST = ["apple", "banana", "watermelon", "grape", "orange"]

def get_random_word():
    return random.choice(WORD_LIST)
