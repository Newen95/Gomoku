## ## EPITECH PROJECT, 2024
## Gomoku
## File description:
## turn

from src.send import send_error
from src.send import send_message
from src.algorithm.ai import ai_algorithm

def turn_command(parts, state):
    if len(parts) != 2:
        return send_error("Invalid number of arguments for TURN command. Expected format: TURN x,y.")
    try:
        x_str, y_str = parts[1].split(',')
        if not x_str.isdigit() or not y_str.isdigit():
            return send_error("Invalid coordinates. It must be numbers.")
        
        x = int(x_str.strip())
        y = int(y_str.strip())

        if x >= state.map.size or y >= state.map.size:
            return send_error("Coordinates out of the map.")
            
        if state.map.update_element(x, y, 2) != "OK":
            return send_error("Something went wrong.")
        
        ai_move = ai_algorithm(state.map.map, time_limit=5, depth=2)
        if ai_move:
            ai_x, ai_y = ai_move
            if state.map.update_element(ai_x, ai_y, 1) == "OK":
                return send_message(f"AI_MOVE {ai_x},{ai_y}")
            else:
                return send_error("AI move failed.")
        else:
            return send_error("AI failed to choose a move.")

    except (IndexError, ValueError):
        return send_error("Invalid format. Expected format: TURN x,y.")

