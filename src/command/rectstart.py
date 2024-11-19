##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## rectstart
##

def rectstart_command(parts, state):
    if len(parts) != 2:
        return "ERROR: Invalid arguments for RECTSTART command. Expected format: RECTSTART width,height."
    try:
        width_str, height_str = parts[1].split(',')
        width = int(width_str.strip())
        height = int(height_str.strip())

        if width <= 0 or height <= 0:
            return "ERROR: Invalid dimensions for RECTSTART. Width and height must be positive."

        state.map.init_tab_rectangular(width, height)
        return "OK: Rectangular board has started."

    except (IndexError, ValueError):
        return "ERROR: Invalid format for RECTSTART command."