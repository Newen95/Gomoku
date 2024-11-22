##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## start
##

from src.send import send_error
from src.send import send_ok

def start_command(parts, state):
    if len(parts) != 2:
        return send_error("Invalid number of arguments.")
    if state.started == True:
        return send_error("The game has already started.")
    try:
        size = int(parts[1])
        if size <= 0 or size > 20:
            return send_error("Invalid board size. It must be between 1 and 20.")
        state.map.init_tab(size)
        state.started = True
<<<<<<< HEAD
        return send_ok("- everything is good")
=======
<<<<<<< HEAD
        return send_message("Game has started.")
=======
        return "OK"
>>>>>>> 685b078 ([ADD] Game settings for gameState)
>>>>>>> 65d2f13 ([ADD] Game settings for gameState)
    except (IndexError, ValueError):
        return send_error("Invalid arguments for START command. Expected format: START size.")