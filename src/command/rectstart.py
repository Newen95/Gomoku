##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## rectstart
##

from src.send import send_error
from src.send import send_message   

def rectstart_command(parts, state):
    if len(parts) != 2:
        return send_error("Invalid arguments for RECTSTART command. Expected format: RECTSTART width,height.")
    try:
        width_str, height_str = parts[1].split(',')
        width = int(width_str.strip())
        height = int(height_str.strip())

        if width <= 0 or height <= 0:
            return send_error("Invalid dimensions for RECTSTART. Width and height must be positive.")

        state.map.init_tab_rectangular(width, height)
        return send_message("Rectangular board has started.")

    except (IndexError, ValueError):
        return send_error("Invalid format for RECTSTART command.")