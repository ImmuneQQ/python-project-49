from brain_games.engine import engine
from random import randint
from prompt import string


def game_prime():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(prime_logic, game_rule)


def prime_logic():
    number = randint(1, 9)
    print(f'Question: {number}')
    answer = string('Your answer: ')
    result = 'yes' if is_prime(number) else 'no'
    if (answer == result):
        return (True,)
    return (False, answer, result)


def is_prime(x):
    if x <= 3:
        return x > 1
    if x % 2 == 0 or x % 3 == 0:
        return False
    limit = int(x**0.5)
    for i in range(5, limit + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True
