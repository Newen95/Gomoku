##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## start
##

def start_command(parts, state):
    if len(parts) != 2:
        return "ERROR: Invalid number of arguments."
    if state.started == True:
        return "ERROR: The game has already started."
    try:
        size = int(parts[1])
        if size <= 0 or size > 20:
            return "ERROR: Invalid board size. It must be between 1 and 20."
        state.map.init_tab(size)
        state.started = True
        return "OK: Game has started."
    except (IndexError, ValueError):
        return "ERROR: Invalid arguments for START command. Expected format: START size."