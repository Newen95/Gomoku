##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## info
##

def info_command(parts, gameState):
    if len(parts) != 3:
        return "ERROR: Incorrect number of arguments."
    
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
    
    action = command_actions.get(parts[1])
    if action is None:
        return f"ERROR: Unknown key '{parts[1]}'. Valid keys are: {', '.join(command_actions.keys())}"

    try:
        return action()
    except ValueError as e:
        return f"ERROR: Invalid value '{parts[2]}' for key '{parts[1]}'. {str(e)}"
    except Exception as e:
        return f"ERROR: {str(e)}"