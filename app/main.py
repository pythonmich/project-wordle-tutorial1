import random
from typing import List

from colorama import Fore, init

from letter_state import LetterState
from wordle import Wordle


def main():
    init()
    word_set = load_word_set('data/wordle_words.txt')
    secret = random.choice(list(word_set))
    wordle = Wordle(secret=secret)

    while wordle.can_attempt:
        x = input('\nType your guess? ').strip().upper()
        
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word must be {wordle.WORD_LENGTH} characters long' + Fore.RESET)
            continue
        
        if not x in word_set:
            print(Fore.RED + f'{x.upper()} not a valid word' + Fore.RESET)
            continue

        wordle.add_attempt(x)
        display_results(wordle=wordle)
    
    if wordle.is_solved:
        print('You\'ve solved the puzzle')     

    else:
        print('You failed to solve the puzzle')
        print(f'The secret word was {wordle.secret}')

def display_results(wordle: Wordle) -> None:
    print('\nYour guess results so far...\n')
    print(f'You have {wordle.remaining_attempts} attempts remaining..\n')
    lines = []

    for word in wordle.attempts:
        results = wordle.guess(word=word)
        colored_result_str = convert_result_color(result=results)
        lines.append(colored_result_str)
    
    for _ in range(wordle.remaining_attempts):
        lines.append(' '.join('_' * wordle.WORD_LENGTH))

    draw_border_around(lines=lines)

# convert_result_color converts results into color for much better output
def convert_result_color(result: List[LetterState]) -> str:
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return ' '.join(result_with_color)


def load_word_set(path: str) -> set:
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def draw_border_around(lines: List[str], size: int=9, padding:int= 1):
    content_length = size + padding * 2
    top_border = '┌' + '─' * content_length + '┐'
    bottom_border = '└' + '─' * content_length + '┘'
    space = ' ' * padding
    print(top_border)

    for line in lines:
        print(f'│{space}{line}{space}│')

    print(bottom_border)

if __name__ == '__main__':
    main()
