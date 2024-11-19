##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## info
##

def info_command(parts, gameState):
    if len(parts) != 3:
        return "ERROR"
    
    command_actions = {
        "timeout_match": lambda: gameState.init_timeout_match(parts),
        "timeout_turn": lambda: gameState.init_timeout_turn(parts),
        "max_memory": lambda: gameState.init_max_memory(parts),
        "time_left": lambda: gameState.init_time_left(parts),
        "game_type": lambda: gameState.init_game_type(parts),
        "rule": lambda: gameState.init_rule(parts),
        "evaluate": lambda: gameState.init_evaluate(parts),
        "print": lambda: gameState.print_all(),
    }
    
    return command_actions.get(parts[1], lambda: "ERROR")()