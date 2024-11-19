##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## command
##

from src.board import board

def start(parts, gameState):
    if gameState.started == True:
        return False
    try:
        val = int(parts[1])

        if val <= 20:
            gameState.map.init_tab(val)
            return True
        return False
    except (IndexError, ValueError):
        return False

def start_command(parts, gameState):
    if len(parts) != 2:
        print ("ERROR message - unsupported size or other error")
        return "ERROR"
    if not start(parts, gameState):
        print ("ERROR message - unsupported size or other error")
        return "ERROR"
    print("OK - everything is good")
    return "START"

def end_command():
    return "END"
    
def turn_command(parts, gameState):
    if len(parts) != 2:
        return False
    if gameState.started == False:
        gameState.started = True
    try:
        x_str, y_str = parts[1].split(',')

        if not x_str.isdigit() or not y_str.isdigit():
            return False

        x = int(x_str.strip())
        y = int(y_str.strip())

        if x >= gameState.map.size or y >= gameState.map.size:
            return False

        if gameState.map.update_element(x, y, 2):
            return True
        return False
    except (IndexError, ValueError):
        return False
    
def begin_command(gameState):
    if gameState.started == True:
        return "ERROR"
    if gameState.map.update_element(11, 10, 1):
        gameState.started = True
        print("11,10")
        return "BEGIN"
    return "ERROR"
    
def board_command(parts, gameState):
    if not board(parts, gameState):
        return "ERROR"
    return "BOARD"

def print_command(gameState):
    gameState.map.print_map()
    return "PRINT"

def about_command():
    return "ABOUT"

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