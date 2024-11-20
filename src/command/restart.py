##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## restart
##

def restart_game_command(state):
    state.map.restart()
    state.started = False
    return "OK: Game has been restarted."