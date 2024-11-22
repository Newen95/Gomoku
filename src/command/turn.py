##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## turn
##

from src.send import send_error
from src.send import send_message   

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

        if state.map.update_element(x, y, 2):
            return send_message("TURN command worked correctly.")
        return send_error("Something went wrong.")
    except (IndexError, ValueError):
        return send_error("Invalid format. Expected format: TURN x,y.")
