##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## begin
##

def begin_command(gameState):
    result = gameState.map.update_element(0, 0, 1)
    if result == "OK":
        print("11,10")
        return "BEGIN"
    else:
        return result

