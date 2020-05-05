from connect4.player.player import Player


class Computer(Player):
    def __init__(self, name, board, strategy):
        super().__init__(name, board)
        self.__strategy = strategy

    def move(self, line, column, value):
        '''
        This function moves for the computer player in the wanted cell.
        :param line: the line number
        :param column: the column number
        :param value: the value of the player
        :return the cell where it moved
        '''
        return self.__strategy.move(self._board, value)
