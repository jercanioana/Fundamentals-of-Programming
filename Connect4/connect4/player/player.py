from abc import abstractmethod

from connect4.board.cell import Cell


class Player:
    def __init__(self, name, board):
        self._name = name
        self._board = board

    @abstractmethod
    def move(self, *args) -> Cell:
        pass
