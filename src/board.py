##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## board
##

def re_init_map(parts, state):
    try:
        x_str, y_str, value = parts.split(',')

        if not x_str.isdigit() or not y_str.isdigit() or not value.isdigit():
            return False
        
        x = int(x_str.strip())
        y = int(y_str.strip())
        val = int(value.strip())

        if x >= state.map.size or y >= state.map.size:
            return False
        if val != 1 or val != 2:
            return False

        if state.map.update_element(x, y, val):
            return True
        return False
    except (ValueError, IndexError):
        return False
        

def board(parts, state):
    if len(parts) != 1:
        return False
    state.map.restart()
    enter = ""
    while enter.lower() != "DONE":
        #print("enter")
        enter = input()
        parts = enter.strip().split()
        if (parts[0] == "DONE"):
            return
        if len(parts) != 1:
            return
        re_init_map(parts[0], state)
        