##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## play
##

def play_command(parts, state):
    if len(parts) != 2:
        return "ERROR: Invalid arguments for PLAY command. Expected format: PLAY x,y."
    try:
        x_str, y_str = parts[1].split(',')

        if not x_str.isdigit() or not y_str.isdigit():
            return "ERROR: Invalid coordinates. They must be numbers."

        x = int(x_str.strip())
        y = int(y_str.strip())

        if x >= state.map.size or y >= state.map.size:
            return "ERROR: Coordinates out of the map."

        if state.map.update_element(x, y, 1):
            return "OK: PLAY command worked correctly."
        return "ERROR: Unable to place the move."
    except (IndexError, ValueError):
        return "ERROR: Invalid format. Expected format: PLAY x,y."
