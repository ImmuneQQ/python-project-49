from brain_games.engine import engine
from random import randint
from prompt import string


def game_progression():
    game_rule = 'What number is missing in the progression?'
    engine(progression_logic, game_rule)


def progression_logic():
    start_number = randint(1, 9)
    progression = randint(1, 9)
    progression_list = [start_number]
    for i in range(9):
        progression_list.append(progression_list[i] + progression)
    hide_index = randint(0, 9)
    hide = progression_list[hide_index]
    progression_list[hide_index] = '..'
    progression_list = [str(i) for i in progression_list]
    progression_str = ' '.join(progression_list)
    print(f'Question: {progression_str}')
    answer = string('Your answer: ')
    if (answer == str(hide)):
        return (True,)
    return (False, answer, hide)
