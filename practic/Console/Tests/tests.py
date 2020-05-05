import unittest

from Domain.entities import Board


class TestCase(unittest):
    def Setup(self):
        board = Board(3,3)
    def test_get_columns(self):
        board = Board(3, 3)
        self.assertequal(board.get_columns(),3)

    def test_get_lines(self):
        board = Board(3, 3)
        self.assertequal(board.get_lines(),3)

    def test_get_cells(self):
        board = Board(3, 3)
        self.assertequal(board.get_cells(),3)

    def test_set_columns_values(self):
        board = Board(3, 3)
        board.set_cell(1,3)

