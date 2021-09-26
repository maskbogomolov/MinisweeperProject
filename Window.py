import random

from Slot import Slot


class Window:
    def __init__(self, weight_size, height_size, n_bombs):
        self.cells = [[Slot(y, x) for x in range(weight_size)] for y in range(height_size)]
        self.weight_size = weight_size
        self.height_size = height_size
        self.n_bombs = n_bombs
        self.open_cells = 0
        self.plant_bomb(n_bombs)
        self.bomb_neighbors()

    def plant_bomb(self, n_bombs):
        sample = [[i, j] for i in range(self.weight_size) for j in range(self.height_size)]

        cells = random.sample(sample, n_bombs)

        for cell in cells:
            self.cells[cell[0]][cell[1]].is_bomb = True
    def bomb_neighbors(self):
        for i in range(self.weight_size):
            for j in range(self.height_size):
                neighs = self.neighbors(i, j)

                ns_with_bombs = [t
                                 for t in neighs
                                 if self.cells[t[0]][t[1]].is_bomb
                                 and not (t[0] == i and t[1] == j)]

                self.cells[i][j].n_bombs = len(ns_with_bombs)

    def neighbors(self, i, j):
        neighbors = [
            (max(0, i - 1), j),
            (max(0, i - 1), max(0, j - 1)),
            (max(0, i - 1), min(self.weight_size - 1, j + 1)),
            (i, min(self.weight_size - 1, j + 1)),
            (i, max(0, j - 1)),
            (min(self.height_size - 1, i + 1), j),
            (min(self.height_size - 1, i + 1), min(self.weight_size - 1, j + 1)),
            (min(self.height_size - 1, i + 1), max(0, j - 1))
        ]

        return list(set(neighbors))

    def open_blank(self, x, y, first):
        if (self.cells[x][y].is_open
                or self.cells[x][y].is_flag):
            return

        neighs = self.neighbors(x, y)

        zero_neighs = [t
                       for t in neighs
                       if self.cells[t[0]][t[1]].is_open and
                       self.cells[t[0]][t[1]].n_bombs == 0
                       ]
        if (not self.cells[x][y].is_bomb
                and (first or len(zero_neighs) != 0)):
            self.cells[x][y].is_open = True
            self.open_cells += 1

            self.cells[x][y].update_char()
        else:
            return

        for t in neighs:
            self.open_blank(t[0], t[1], False);

    def update(self, x, y, command):
        if (command == 'Flag'):
            self.cells[x][y].is_flag = True
        elif (command == 'Unflag'):
            self.cells[x][y].is_flag = False
        elif (self.cells[x][y].is_bomb):
            self.cells[x][y].is_open = True
            print("here")
            self.cells[x][y].update_char()
            return True
        elif (command == 'Open'):
            self.open_blank(x, y, True)
        else:
            print("Unknown command")

        self.cells[x][y].update_char()
        return self.end_game()

    def coords_in_range(self, x, y):
        return not (x < 0 or x >= self.weight_size or y < 0 or y >= self.height_size)

    def end_game(self):
        return self.weight_size * self.height_size - self.open_cells == self.n_bombs

    def print_cells(self):

        for i in range(self.weight_size):
            print(i+1,"|", end=" ")
            for j in range(self.height_size):
                print(self.cells[i][j].char, end=" ")
            print("|")

    def print_info(self):
        for i in range(self.weight_size):
            for j in range(self.height_size):
                self.cells[i][j].print_info()
            print()