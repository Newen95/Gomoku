##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## print
##

from src.send import send_message   

def print_command(state):
    state.map.print_map()
    return send_message("PRINT")
