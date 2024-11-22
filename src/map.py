##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## map
##

from src.send import send_error
from src.send import send_message   

class Map:
    
    def __init__(self):
        self.history = []

    def takeback(self):
        if not self.history:
            return False
        x, y, value = self.history.pop()
        self.map[y][x] = 0
        return True

    def init_tab(self, size):
        self.size = size
        self.map = [[0 for _ in range(size)] for _ in range(size)]

    def init_tab_rectangular(self, width, height):
        self.size_x = width
        self.size_y = height
        self.map = [[0 for _ in range(width)] for _ in range(height)]

    def restart(self):
        self.map = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def update_element(self, x, y, value):
        if x >= self.size or y >= self.size:
            return send_error(f"Position ({x}, {y}) is out of the map. The board size is {self.size}x{self.size}.")
        if self.map[y][x] != 0:
            return send_error(f"Cell ({x}, {y}) is already occupied.")
        if value not in (1, 2):
            return send_error("Invalid value. Allowed values are 1 or 2.")
        
        self.map[y][x] = value
        self.history.append((x, y, value))
        return send_message("OK")


    def print_map(self):
        for ligne in self.map:
            print (" ".join(map(str, ligne)))