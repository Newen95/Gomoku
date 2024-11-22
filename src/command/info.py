##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## info
##

from src.send import send_error
from src.gameState import GameState

def info_command(parts = list, gameState = GameState):
    settings : dict = gameState.settings
    if len(parts) != 3:
        return send_error("Info command - Incorrect number of arguments.")
    if parts[1] not in settings.keys():
        return send_error("Info -command - Incorrect key")
    key = parts[1]
    value = parts[2]

    gameState.settings[key] = int(value)
    