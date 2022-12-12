from brain_games.engine import engine
from random import randint
from prompt import string


def game_calc():
    game_rule = 'What is the result of the expression?'
    engine(calc_logic, game_rule)


def calc_logic():
    number1 = randint(1, 9)
    number2 = randint(1, 9)
    operations = ('+', '-', '*')
    operation = operations[randint(0, 2)]
    print(f'Question: {number1} {operation} {number2}')
    answer = string('Your answer: ')
    if operation == '+':
        result = number1 + number2
    if operation == '-':
        result = number1 - number2
    if operation == '*':
        result = number1 * number2
    if (answer == str(result)):
        return (True,)
    return (False, answer, result)
