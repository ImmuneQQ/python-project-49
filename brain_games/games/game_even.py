from brain_games.games.games_logic import run_game, even_logic


def game_even():
    game_rule = 'What is the result of the expression?'
    run_game(even_logic, game_rule)
