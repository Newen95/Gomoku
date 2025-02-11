##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

from src.send import send_error
from src.send import send_message
from src.gameState import GameState

def begin_command(parts : list, state : GameState):
    if len(parts) != 1:
        send_error("Begin command - No arguments expected")
        return
    if not state.started:
        return send_error("Begin command - Game has not been started yet")
    x = int(state.map.size/2)
    y = int(state.map.size/2)
    result = state.map.update_element(x, y, 1)
    return f'{x},{y}'
