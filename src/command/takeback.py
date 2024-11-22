##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## takeback
##

from src.send import send_error
from src.send import send_message   

def takeback_command(parts, state):
    if len(parts) != 2:
        return send_error("Invalid arguments for TAKEBACK command. Expected format: TAKEBACK x,y.")
    try:
        x_str, y_str = parts[1].split(',')
        x = int(x_str.strip())
        y = int(y_str.strip())
        if state.map.takeback():
            return send_message("Takeback command worked correctly.")
        return send_error("Unable to take back move.")
    except (IndexError, ValueError):
        return send_error("Invalid coordinates.")