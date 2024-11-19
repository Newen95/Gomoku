##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## parse
##

from src.board import board

def play(parts, state):
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

def takeback(parts, state):
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

def rectstart(parts, state):
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

def restart_game(state):
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.restart()
    state.started = False
    return "OK: Game has been restarted."

def start(parts, state):
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

def turn(parts, state):
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
        
def parse(enter, state):
    parts = enter.strip().split()
    command = parts[0].upper() if parts else ""

    if command == "END":
        return "END"
    elif command == "START":
        return start(parts, state)
    elif command == "TURN":
        return turn(parts, state)
    elif command == "BEGIN":
        state.starter = True
        enter = input("Entrer position: ").strip
        print(enter)
    elif command == "BOARD":
        if not state.started:
            return "ERROR: The game has not started yet."
        if not board(parts, state):
            return "ERROR: Invalid board format."
        return "BOARD"
    elif command == "INFO":
        return "INFO"
    elif command == "ABOUT":
        return "ABOUT"
    elif command == "PRINT":
        if not state.started:
            return "ERROR: The game has not started yet."
        state.map.print_map()
        return "PRINT"
    elif command == "RESTART":
        return restart_game(state)
    elif command == "RECTSTART":
        return rectstart(parts, state)
    elif command == "TAKEBACK":
        return takeback(parts, state)
    elif command == "PLAY":
        return play(parts, state)
    else:
        return "ERROR: Unknown command"
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.restart()
    state.started = False
    return "OK: Game has been restarted."