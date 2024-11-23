##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

from src.send import send_error

def begin_command(gameState):
    result = gameState.map.update_element(11, 10, 1)
    if result == "OK":
        return "11,10"
    return send_error(result)
