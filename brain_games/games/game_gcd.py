from brain_games.games.games_logic import run_game, gcd_logic


def game_gcd():
    game_rule = 'What is the result of the expression?'
    run_game(gcd_logic, game_rule)
