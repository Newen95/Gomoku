##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## info
##

from src.send import send_error
from src.gameState import GameState

def info_command(parts = list, state = GameState):
    settings : dict = state.settings
    if len(parts) != 3:
        return send_error("Info command - Incorrect number of arguments.")
    if parts[1] not in settings.keys():
        return send_error("Info command - Incorrect key")
    key = parts[1]
    value = parts[2]

<<<<<<< HEAD
    gameState.settings[key] = int(value)
=======
    settings[key] = int(value)

    print("current settings: settings", settings)
>>>>>>> 50e9504569e2068e7b66fa7d0a094dc60b139e26
    
