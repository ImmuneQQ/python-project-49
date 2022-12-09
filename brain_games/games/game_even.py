from brain_games.games.run_game import run_game
from random import randint
from prompt import string


def game_even():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(even_logic, game_rule)


def even_logic():
    number = randint(1, 9)
    print(f'Question: {number}')
    answer = string('Your answer: ')
    result = 'no' if number % 2 else 'yes'
    if answer == result:
        return (True,)
    return (False, answer, result)
