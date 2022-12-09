from prompt import string


def run_game(game_logic, game_rule):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
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
