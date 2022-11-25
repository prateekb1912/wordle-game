from rich.console import Console
from rich.prompt import Prompt
from random import choice

with open('popular_words_5000.txt', 'r') as file:
    words = []

    for line in file.readlines():
        word = line.strip()
        words.append(word)

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
ALLOWED_GUESSES = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


GUESS_STATEMENT = "\nEnter your guess"

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

def check_guess(guess, answer):
    guessed = []
    pattern = []

    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            pattern.append(SQUARES['incorrect_letter'])
    
    return ''.join(guessed), ''.join(pattern)

def game(console, chosen_word):
    game_end = False
    already_guessed = []
    patterns = []
    all_words_guessed = []

    while not game_end:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print("[red]Please enter a 5-letter word!\n[/]")
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        patterns.append(pattern)

        console.print(*all_words_guessed, sep='\n')
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            game_end = True
        
        if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
            console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
            console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]YOUR SCORE: {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    
    console.print(*patterns, sep="\n")



if __name__ == '__main__':
    console = Console()

    chosen_word = choice(words).upper()
    console.print(WELCOME_MESSAGE)

    game(console, chosen_word)
