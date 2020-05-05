from Domain.entities import Board
from Repository.repo import Player, Human, Computer
import random

class Console:
    def __init__(self, repo):
        self.__repo = repo
        self.__board = Board(3,3)

    def run_menu(self):
        while True:
            try:
                print("1. Start playing.")
                cmd = int(input("Enter a command: "))
                if cmd == 1:
                    self.__start()
                else:
                    break

            except ValueError as ve:
                print(ve)

    def __start(self):
        n = 0
        turn = 0
        k = 0
        print(Board(3,3).print_board())
        while k < 9:
            if turn % 2 == 0:
                col = int(input("Enter a line: "))
                if 0 < col < 9:
                    pass
                else:
                    raise ValueError("Invalid number.")
                # self.__repo.move_human(col-1, 'X')
                k += 1
                print(self.__board.set_cell(col-1, 'X'))

                turn += 1

            if turn % 2 == 1 and n < 4:
                self.__repo.move_computer(n, 'O')
                n += 1
                k += 1
                print(self.__board.set_cell(n, 'O'))
                turn += 1










