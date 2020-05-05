import numpy as np
from texttable import Texttable
from connect4.board.cell import Cell


class Board:
    def __init__(self, empty_value = 0):

        self.__empty_value = empty_value
        self.__cells = self.__create_board()

    def __create_board(self):

        '''
        This function creates the board for the game
        :return: the board
        '''

        board = np.zeros((6 , 7))
        return board

    def get_line_values(self, line):
        '''
        This function returns all the values on the given line.
        :param line: line number
        :return: values
        '''
        return self.__cells[line]

    def get_column_values(self, column):
        '''
        This function returns all the values on the given column.
        :param column: column number
        :return: values
        '''
        return [int(self.__cells[i][column]) for i in range(6)]

    def get_value(self, line, column):
        '''
        This function returns the value of the certain cell.
        :param line: the line number
        :param column: the column number
        :return: the value of the cell
        '''
        return int(self.__cells[line][column])

    def set_value(self, line, column, value):
        '''
        This function sets the value of the specified cell.
        :param line: the line number
        :param column: the column number
        :param value: the player's value

        '''
        self.__cells[line][column] = value

    def get_empty_cells(self):
        '''
        Returns all the empty cells
        :return: the cells without any values
        '''
        return [cell for cell in self.get_all_cells()
                if cell.value == self.__empty_value]

    def get_all_cells(self):
        '''

        :return: all the cells of the board
        '''
        res = []
        for i in range(6):
            for j in range(7):
                res.append(Cell(i, j, self.__cells[i][j]))
        return res

    def get_cells_values(self):
        '''
        This function returns the values of all the cells from the board.
        :return: the values of the cells
        '''
        return int(self.__cells)

    def is_valid(self, column):
        '''
        This function checks whether a move is valid or not.
        :param column: the given column number
        :return: True of False
        '''
        if column < 0 or column > 7:
            return False
        return True

    def get_lowest_point(self, column):
        '''
        This function determines the lowest point where we can place a value.
        :param column: the column number
        :return: the lowest point without any value
        '''
        for j in range(5, -1, -1):
            if self.get_value(j,column) == 0:
                return j
        return -1

    def is_winner(self, value):
        '''
        This function check whether we have the same value on 4 consecutive positions on the lines, columns or diagonals.
        :param value: the value of the cell
        :return: True, if we have a winner, false otherwise
        '''
        #check lines
        for i in range (6):
            for j in range (4):
                if self.__cells[i][j] == value and self.__cells[i][j+1] == value and self.__cells[i][j+2] == value and self.__cells[i][j+3] == value:
                    return True

        #check columns
        for i in range (3):
            for j in range (7):
                if self.__cells[i][j] == value and self.__cells[i+1][j] == value and self.__cells[i+2][j] == value and self.__cells[i+3][j] == value:
                    return True

        #check diagonals
        for i in range (3):
            for j in range (4):
                if self.__cells[i][j] == value and self.__cells[i+1][j+1] == value and self.__cells[i+2][j+2] == value and self.__cells[i+3][j+3] == value:
                    return True

        #check diagonals
        for i in range (3):
            for j in range (3, 7):
                if self.__cells[i][j] == value and self.__cells[i+1][j-1] == value and self.__cells[i+2][j-2] == value and self.__cells[i+3][j-3] == value:
                    return True


    def __str__(self):
        res = Texttable()
        for line in self.__cells:
            s = " ".join([str(int(value)) for value in line]) + "\n"
            res.add_row(s)
        return res.draw()

