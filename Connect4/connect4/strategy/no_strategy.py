from connect4.board.cell import Cell
from connect4.strategy.strategy import Strategy


class NoStrategy(Strategy):
    def move(self, board, value):
        '''
        This function makes the moves of the AI in order to block the opponent to win.
        :param board: the board of the game
        :param value:
        :return:
        '''
        empty = board.get_empty_cells()
        if len(empty) == 0:
            return None
        line = board.get_lowest_point(empty[0].column)
        column = empty[0].column

        nr = self.move_lines(board, value)
        if nr is not None:
            line = nr[0]
            column = nr[1]

        elif self.move_columns(board, value):
            nr = self.move_columns(board, value)
            line = nr[0]
            column = nr[1]

        elif self.move_diagonals(board, value):
            nr = self.move_diagonals(board, value)
            line = nr[0]
            column = nr[1]

        elif self.block_lines(board):
            nr = self.block_lines(board)
            line = nr[0]
            column = nr[1]

        elif self.block_columns(board):
            nr = self.block_columns(board)
            line = nr[0]
            column = nr[1]

        elif self.block_diagonals(board):
            nr = self.block_diagonals(board)
            line = nr[0]
            column = nr[1]

        board.set_value(line, column, value)
        return Cell(line, column, value)

    def move_lines(self, board, value):
        '''
        This function determines the next position where the AI could move.
        :param board: the game board
        :param value: the value
        :return:
        '''
        for i in range (6):
            for j in range (4):
                if board.get_value(i,j) == value and board.get_value(i, j+1) == value and board.get_value(i, j+2) ==\
                        value and board.get_value(i, j+3) == 0 and board.get_lowest_point(j+3) == i:
                    return i, j+3
        return None

    def move_columns(self, board, value):
        '''
        This function determines the next position where the AI could move.
            :param board: the game board
            :param value: the value

        '''
        for i in range (3):
            for j in range (7):
                if board.get_value(i, j) == value and board.get_value(i+1, j) == value and board.get_value(i+2, j) ==\
                        value and board.get_value(i+3, j) == 0 and board.get_lowest_point(j) == i+3:
                    return i+3, j
        return None

    def move_diagonals(self, board, value):
        '''
        This function determines the next position where the AI could move.
        :param board: the game board
        :param value: the value

        '''
        for i in range (3):
            for j in range (4):
                if board.get_value(i, j) == value and board.get_value(i+1, j+1) == value and board.get_value(i+2, j+2)\
                        == value and board.get_value(i+3, j+3) == 0 and board.get_lowest_point(j+3) == i+3:
                    return i+3, j+3
        for i in range(3):
            for j in range(3, 7):
                if board.get_value(i, j) == value and board.get_value(i + 1, j - 1) == value and \
                        board.get_value(i + 2,j - 2) == value and board.get_value(i + 3, j - 3) == 0 and board.get_lowest_point(j-3) == i+3:
                    return i+3, j-3

        return None

    def block_lines(self, board):
        '''
        This function determines the best position for the AI to move in order to prevent the other player to win on the
         lines.
        :param board: the game board
        :return:
        '''
        for i in range(6):
            for j in range(4):
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 2 and board.get_value(i, j + 2) == 2 and\
                        board.get_value(i, j + 3) == 0 and board.get_lowest_point(j+3) == i:
                    return i, j + 3
                if board.get_value(i, j) == 0 and board.get_value(i, j + 1) == 2 and board.get_value(i, j + 2) == 2 and\
                        board.get_value(i, j + 3) == 2 and board.get_lowest_point(j) == i:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 0 and board.get_value(i, j + 2) == 2 and\
                        board.get_value(i, j + 3) == 2 and board.get_lowest_point(j+1) == i:
                    return i, j+1
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 2 and board.get_value(i, j + 2) == 0 and\
                        board.get_value(i, j + 3) == 2 and board.get_lowest_point(j+2) == i:
                    return i, j+2
        return None

    def block_columns(self, board):
        '''
        This function determines the best position for the AI to move in order to prevent the other player to win on the
         columns.
        :param board: the game board

        '''
        for i in range (3):
            for j in range (7):
                if board.get_value(i, j) == 0 and board.get_value(i+1, j) == 2 and board.get_value(i + 2, j) == 2 and\
                        board.get_value(i+3, j) == 2 and board.get_lowest_point(j) == i:
                    return i, j
        return None

    def block_diagonals(self, board):
        '''
        This function determines the best position for the AI to move in order to prevent the other player to win on the
         diagonals.
        :param board: the game board

        '''
        for i in range (3):
            for j in range (4):
                if board.get_value(i, j) == 0 and board.get_value(i+1, j+1) == 2 and board.get_value(i + 2, j+2) == 2 \
                        and board.get_value(i + 3, j + 3) == 2 and board.get_lowest_point(j) == i:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i+1, j+1) == 0 and board.get_value(i + 2, j+2) == 2 \
                        and board.get_value(i + 3, j + 3) == 2 and board.get_lowest_point(j+1) == i+1:
                    return i + 1, j + 1
                if board.get_value(i, j) == 2 and board.get_value(i+1, j+1) == 2 and board.get_value(i + 2, j+2) == 0 \
                        and board.get_value(i + 3, j + 3) == 2 and board.get_lowest_point(j+2) == i+2:
                    return i + 2, j + 2
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j + 1) == 2 and board.get_value(i + 2, j+2)==\
                        2 and board.get_value(i + 3, j + 3) == 0 and board.get_lowest_point(j + 3) == i+3:
                    return i + 3, j + 3

        for i in range (3):
            for j in range (3, 7):
                if board.get_value(i, j) == 0 and board.get_value(i+1, j - 1) == 2 and board.get_value(i + 2, j-2) == 2\
                        and board.get_value(i + 3, j - 3) == 2 and board.get_lowest_point(j) == i:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i+1, j - 1) == 0 and board.get_value(i + 2, j-2) == 2\
                        and board.get_value(i + 3, j - 3) == 2 and board.get_lowest_point(j-1) == i+1:
                    return i + 1, j - 1
                if board.get_value(i, j) == 2 and board.get_value(i+1, j - 1) == 2 and board.get_value(i + 2, j-2) == 0\
                        and board.get_value(i + 3, j - 3) == 2 and board.get_lowest_point(j-2) == i+2:
                    return i + 2, j - 2
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j - 1) == 2 \
                        and board.get_value(i + 2, j-2) == 2 and board.get_value(i + 3, j - 3) == 0 and\
                        board.get_lowest_point(j - 3) == i + 3:
                    return i + 3, j - 3

        return None