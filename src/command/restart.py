##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## restart
##

def restart_game_command(state):
    if not state.started:
        return "ERROR: The game has not started yet."
    state.map.restart()
    state.started = False
    return "OK: Game has been restarted."