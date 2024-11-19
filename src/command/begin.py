##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

def begin_command(gameState):
    if gameState.started == True:
        return "ERROR"
    gameState.starter = True
    if gameState.map.update_element(11, 10, 1):
        gameState.started = True
        print("11,10")
        return "BEGIN"
    return "ERROR"

