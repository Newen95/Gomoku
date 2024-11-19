##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## turn
##

def turn_command(parts, state):
    if len(parts) != 2:
        return "ERROR: Invalid number of arguments for TURN command. Expected format: TURN x,y."
    if not state.started:
        return "ERROR: The game has not started yet."
    try:
        x_str, y_str = parts[1].split(',')

        if not x_str.isdigit() or not y_str.isdigit():
            return "ERROR: Invalid coordinates. It must be numbers."

        x = int(x_str.strip())
        y = int(y_str.strip())

        if x >= state.map.size or y >= state.map.size:
            return "ERROR: Coordinates out of the map."

        if state.map.update_element(x, y, 2):
            return "OK: TURN command worked correctly."
        return "ERROR: Something went wrong."
    except (IndexError, ValueError):
        return "ERROR: Invalid format. Expected format: TURN x,y."
