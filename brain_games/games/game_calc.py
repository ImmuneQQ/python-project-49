from brain_games.games.games_logic import run_game, calc_logic


def game_calc():
    game_rule = 'What is the result of the expression?'
    run_game(calc_logic, game_rule)
