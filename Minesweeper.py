import pickle

from Window import Window

class Minesweeper:

    @staticmethod
    def start():
        print("Выберите режим указав номер. 1.Обычная игра(5x5) 2.Своя игра 3.Загрузить последнюю")
        inp = input()
        if inp == '1':
            window = Window(5,5, 5)
        if inp == '2':
            print("Введите значения ")
            weight_size, height_size, nun_bombs = map(int, input().split())
            window = Window(weight_size, height_size, nun_bombs)

        if inp == '3':
            with open('save_game.pkl', 'rb') as f:
                window = pickle.load(f)
        Minesweeper.logic(window)

    @staticmethod
    def logic(window):
        window.print_cells()
        while (True):
            print("Вам нужно выбрать ячейку и выбрать действие (Open or Flag)", end=" ")
            inp = input()
            x, y, command = inp.split()
            x = int(x) - 1
            y = int(y) - 1

            is_end = False
            if window.coords_in_range(x, y):
                is_end = window.update(x, y, command)

            window.print_cells()

            if is_end:
                print("Похоже вы взорвались.Сохраним игру? Напишите Save")
                inp = input()
                if inp == 'Save':
                    with open('save_game.pkl', 'wb') as f:
                        pickle.dump(window, f, protocol=5)
                break

