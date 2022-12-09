import random
import prompt


def run_game(game_logic, game_rule):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_rule)
    corrects_count = 0
    for i in range(3):
        game_result = game_logic()
        is_correct = game_result[0]
        if is_correct:
            corrects_count += 1
            print('Correct!')
        else:
            answer = game_result[1]
            result = game_result[2]
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    if corrects_count == 3:
        print(f'Congratulations, {name}!')


def even_logic():
    number = random.randint(1, 9)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    result = 'no' if number % 2 else 'yes'
    if answer == result:
        return (True,)
    return (False, answer, result)


def calc_logic():
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    operations = ('+', '-', '*')
    operation = operations[random.randint(0, 2)]
    print(f'Question: {number1} {operation} {number2}')
    answer = prompt.string('Your answer: ')
    if operation == '+':
        result = number1 + number2
    if operation == '-':
        result = number1 - number2
    if operation == '*':
        result = number1 * number2
    if (answer == str(result)):
        return (True,)
    return (False, answer, result)


def gcd_logic():
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    print(f'Question: {number1} {number2}')
    answer = prompt.string('Your answer: ')
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    result = number1 + number2
    if (answer == str(result)):
        return (True,)
    return (False, answer, result)


def progression_logic():
    start_number = random.randint(1, 9)
    progression = random.randint(1, 9)
    progression_list = [start_number]
    for i in range(9):
        progression_list.append(progression_list[i] + progression)
    hide_index = random.randint(0, 9)
    hide = progression_list[hide_index]
    progression_list[hide_index] = '..'
    progression_list = [str(i) for i in progression_list]
    progression_str = ' '.join(progression_list)
    print(f'Question: {progression_str}')
    answer = prompt.string('Your answer: ')
    if (answer == str(hide)):
        return (True,)
    return (False, answer, hide)
