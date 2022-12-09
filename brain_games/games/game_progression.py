from brain_games.games.games_logic import run_game, progression_logic


def game_progression():
    game_rule = 'What number is missing in the progression?'
    run_game(progression_logic, game_rule)
