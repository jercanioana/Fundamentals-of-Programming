
class Cell:
    def __init__(self, line, column):
        self.__line = line
        self.__column = column

    def __str__(self) -> str:
        return '{0},{1}'.format(self.__line, self.__column)

class Board:
    def __init__(self, lines, columns):
        self.__lines = lines
        self.__columns = columns
        self.__cell = Cell(1,1)
        self.__cells = []
        for i in range(3):
            for j in range(3):
                self.__cells.append(0)


    def get_lines(self):
        '''
        We get all the lines
        :return:
        '''
        return self.__lines

    def get_columns(self):
        '''
        We get all the columns
        :return:
        '''
        return self.__columns

    def get_cells(self):
        '''
        We get all the cells
        :return:
        '''
        return self.__cells

    def set_lines(self, value):
        self.__lines = value

    def set_columns(self, value):
        self.__columns = value


    def set_cell(self, col, value):
        for j in range(9):
            if j == col:
                self.__cells[j] = value
                return self.__cells

    def get_line_value(self,value):
        return self.__lines[value]

    def get_columns_value(self, value):
        return self.__cells[value]

    def print_board(self):
        return self.__cells

    def is_valid(self):
        '''
        Checks whether a move is valid

        '''
        for j in range (9):
            if self.__cells[j] != 0:
                return False
            return True







