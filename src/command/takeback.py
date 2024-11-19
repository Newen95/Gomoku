##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## takeback
##

def takeback_command(parts, state):
    if len(parts) != 2:
        return "ERROR: Invalid arguments for TAKEBACK command. Expected format: TAKEBACK x,y."
    try:
        x_str, y_str = parts[1].split(',')
        x = int(x_str.strip())
        y = int(y_str.strip())
        if state.map.takeback():
            return "OK: Takeback command worked correctly."
        return "ERROR: Unable to take back move."
    except (IndexError, ValueError):
        return "ERROR: Invalid coordinates."