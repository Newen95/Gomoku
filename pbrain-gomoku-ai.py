##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## pbrain-gomoku-ai
##

from src.gameState import GameState
from src.board import board

def start(parts, state):
    if len(parts) != 2 and state.started == True:
        return False
    try:
        val = int(parts[1])

        if val <= 20:
            state.map.init_tab(val)
            return True
        return False
    except (IndexError, ValueError):
        return False
    

def turn(parts, state):
    if len(parts) != 2:
        return False
    if state.started == False:
        state.started = True
    try:
        x_str, y_str = parts[1].split(',')

        if not x_str.isdigit() or not y_str.isdigit():
            return False

        x = int(x_str.strip())
        y = int(y_str.strip())

        if x >= state.map.size or y >= state.map.size:
            return False

        if state.map.update_element(x, y, 2):
            return True
        return False
    except (IndexError, ValueError):
        return False
        
def parse(enter, state):
    parts = enter.strip().split()
    command = parts[0].upper() if parts else ""

    if command == "END":
        return "END"
    elif command == "START":
        if not start(parts, state):
            print ("ERROR message - unsupported size or other error")
        print("OK - everything is good")
    elif command == "TURN":
        turn(parts, state)
    elif command == "BEGIN":
        state.starter = True
        enter = input("Entrer position: ").strip
        print(enter)
    elif command == "BOARD":
        if not board(parts, state):
            return "ERROR"
        return "BOARD"
    elif command == "INFO":
        return "INFO"
    elif command == "ABOUT":
        return "ABOUT"
    elif command == "PRINT":
        state.map.print_map()
        return "PRINT"
    else:
        return "ERROR"

def run():
    enter = ""
    state = GameState()
    while enter.lower() != "END":
        enter = input()
        type = parse(enter, state)
        #print(type)
        if type == "END":
            return

if __name__ == "__main__":
    run()

