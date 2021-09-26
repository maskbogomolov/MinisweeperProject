class Slot:
    def __init__(self, x, y):
        self.is_bomb = False
        self.n_bombs = 0
        self.is_flag = False
        self.is_open = False
        self.char = "_"
        self.x = x
        self.y = y

    def update_char(self):
        if (self.is_flag):
            self.char = '?'
        elif (not self.is_open):
            self.char = '_'
        elif (self.is_bomb):
            self.char = 'Bum'
        elif (self.n_bombs != 0):
            self.char = str(self.n_bombs)
        else:
            self.char = " "

    def print_info(self):
        print(self.is_open, end=" ")
        print(self.is_bomb, end=" ")
        print(self.n_bombs, end=" ")
        print(self.is_flag, end=" ")
        print(self.char)


