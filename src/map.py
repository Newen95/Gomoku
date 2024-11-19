##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## map
##

class Map:
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
        if x < self.size and y < self.size:
            if self.map[y][x] == 0:
                self.map[y][x] = value
                return True
        return False

    def print_map(self):
        for ligne in self.map:
            print (" ".join(map(str, ligne)))