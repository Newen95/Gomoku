##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

def begin_command(gameState):
    if gameState.map.update_element(11, 10, 1):
        print("11,10")
        return "BEGIN"
    return "ERROR"

