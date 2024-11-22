##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## gameState
##

from src.map import Map

class GameState:
    def __init__(self):
        self.map = Map()
        self.started = False
        self.settings = {
            "timeout_match": 0,
            "timeout_turn": 0,
            "max_memory": 0,
            "time_left": 0,
            "game_type": 0,
            "rule": 0,
            "evaluate": 0
        }
   
