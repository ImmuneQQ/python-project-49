import random
import prompt


def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = random.randint(1, 99)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        is_even_number = random_number % 2
        if (answer == 'no' and is_even_number) or (answer == 'yes' and not is_even_number):
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
