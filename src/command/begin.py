##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

from src.send import send_error
from src.send import send_message

def begin_command(gameState):
    result = gameState.map.update_element(0, 0, 1)
    if result == "OK":
        print("11,10")
        return send_message("BEGIN")
    else:
        return send_error(result)

