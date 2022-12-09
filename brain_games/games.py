import random
import prompt


def game_even():
    game(even_check)


def game_calc():
    game(calc_check)


def game(check_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    corrects_count = 0
    for i in range(3):
        if check_func():
            corrects_count += 1
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            break
    if corrects_count == 3:
        print(f'Congratulations, {name}!')


def even_check():
    number = random.randint(1, 9)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    is_even_number = number % 2
    if answer == 'yes' and not is_even_number:
        return True
    if answer == 'no' and is_even_number:
        return True
    return False


def calc_check():
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
        return True
    return False
