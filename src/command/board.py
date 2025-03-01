##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## board
##

from src.send import send_error
from src.send import send_message   
from src.algorithm.ai import ai_algorithm

def re_init_map(line, state):
    try:
        parts = line.split(',')
        if len(parts) != 3:
            return False
        x_str, y_str, value = parts
        if not x_str.strip().isdigit() or not y_str.strip().isdigit() or not value.strip().isdigit():
            return False
        x = int(x_str.strip())
        y = int(y_str.strip())
        val = int(value.strip())
        if x >= state.map.size or y >= state.map.size:
            return False
        if val < 1 or val > 2:
            return False
        return state.map.update_element(x, y, val) == "OK"
    except Exception:
        return False

def board(parts, state):
    if len(parts) != 1:
        return False
    state.map.restart()
    
    while True:
        try:
            enter = input()
        except EOFError:
            return False
        if not enter.strip():
            continue
        line_parts = enter.strip().split()
        if len(line_parts) == 0:
            continue
        if line_parts[0].upper() == "DONE":
            return True
        if len(line_parts) != 1:
            return False
        if not re_init_map(line_parts[0], state):
            return False

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
