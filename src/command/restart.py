##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## restart
##

from src.send import send_ok   

def restart_game_command(state):
    state.map.restart()
    state.started = False
    return send_ok("")