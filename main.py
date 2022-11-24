from rich.console import Console
from random import choice

with open('popular_words_5000.txt', 'r') as file:
    words = []

    for line in file.readlines():
        word = line.strip()
        words.append(word)

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
ALLOWED_GUESSES = 6



if __name__ == '__main__':
    console = Console()

    chosen_word = choice(words)
    console.print(WELCOME_MESSAGE)
    console.print(chosen_word)