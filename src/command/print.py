##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## print
##

def print_command(state):
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.print_map()
    return "PRINT"
