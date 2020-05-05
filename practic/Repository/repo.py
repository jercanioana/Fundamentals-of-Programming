from Domain.entities import Cell, Board


class Game:

    def __init__(self, file_name):
        self.__board = Board(3,3)
        self.__file_name = file_name

    def move(self, args) -> Cell:
        pass

    def move_computer(self, col, args):
        '''
        This function makes a move for the human part

        '''
        for column in range(9):
            if col == column:
                if self.__board.is_valid() == True:
                    self.__board.set_cell(col-1, args)
                    return self.__board.print_board()

    def move_human(self, col, args):
        '''

        This function makes a move for the human part
        '''
        for column in range(9):
            if col == column:
                if self.__board.is_valid() == True:
                    self.__board.set_cell(col-1, args)
                    return self.__board.print_board()


class Player():
    def __init__(self):
        pass

class Human():
    def __init__(self, args):
        self.__human = Player()



class Computer():
    def __init__(self, args):
        self.__computer = Player()










