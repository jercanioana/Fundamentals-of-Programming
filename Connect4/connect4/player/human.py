from connect4.board.cell import Cell
from connect4.player.player import Player


class Human(Player):

    def move(self, line, column, value):
        '''
        This function moves for the human player in the wanted cell.
        :param line: the line number
        :param column: the column number
        :param value: the value of the player
        :return: the cell where we moved
        '''
        self._board.set_value(line, column, value)
        return Cell(line, column, value)
