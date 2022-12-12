from brain_games.engine import engine
from random import randint
from prompt import string


def game_even():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(even_logic, game_rule)


def even_logic():
    number = randint(1, 9)
    print(f'Question: {number}')
    answer = string('Your answer: ')
    result = 'no' if number % 2 else 'yes'
    if answer == result:
        return (True,)
    return (False, answer, result)
