from brain_games.games.run_game import run_game
from random import randint
from prompt import string


def game_gcd():
    game_rule = 'Find the greatest common divisor of given numbers.'
    run_game(gcd_logic, game_rule)


def gcd_logic():
    number1 = randint(1, 9)
    number2 = randint(1, 9)
    print(f'Question: {number1} {number2}')
    answer = string('Your answer: ')
    result = gcd(number1, number2)
    if (answer == str(result)):
        return (True,)
    return (False, answer, result)


def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return y + x
