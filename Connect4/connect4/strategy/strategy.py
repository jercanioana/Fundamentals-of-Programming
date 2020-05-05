from abc import abstractmethod

from connect4.board.cell import Cell

class Strategy:

    @abstractmethod
    def move(self, *args) -> Cell:

        pass