##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## board
##

from src.send import send_error
from src.send import send_message   
from src.algorithm.ai import ai_algorithm

def re_init_map(parts, state):
    try:
        x_str, y_str, value = parts.split(',')

        if not x_str.isdigit() or not y_str.isdigit() or not value.isdigit():
            return False
        
        x = int(x_str.strip())
        y = int(y_str.strip())
        val = int(value.strip())

        if x >= state.map.size or y >= state.map.size:
            return False
        if val < 1 or val > 2:
            return False

        if state.map.update_element(x, y, val) == "OK":
            return True
        return False
    except (ValueError, IndexError):
        return False
        

def board(parts, state):
    if len(parts) != 1:
        return False
    state.map.restart()
    enter = ""
    while enter.lower() != "DONE":
        enter = input()
        parts = enter.strip().split()
        if (parts[0] == "DONE"):
            return True
        if len(parts) != 1:
            return False
        re_init_map(parts[0], state)
        
def board_command(parts, gameState):
    if not board(parts, gameState):
        return send_error("Invalid board format.")
    ai_move = ai_algorithm(gameState.map.map, gameState.map.size)
    if ai_move:
        ai_x, ai_y = ai_move
        if gameState.map.update_element(ai_x, ai_y, 1) == "OK":
            return send_message(f"{ai_x},{ai_y}")
        else:
             return send_error("AI move failed.")
    else:
        return send_error("AI failed to choose a move.")

