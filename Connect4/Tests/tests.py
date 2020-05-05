import unittest

from connect4.board.board import Board
from connect4.board.cell import Cell


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.__board = Board()


    def test_get_line_values(self):
        self.__board.set_value(0, 0, 2)
        values = self.__board.get_line_values(0)
        self.assertEqual(values[0], 2)

    def test_get_column_values(self):
        self.__board.set_value(0, 0, 2)
        values = self.__board.get_column_values(0)
        self.assertEqual(values[0], 2)

    def test_get_value(self):
        self.__board.set_value(0, 0, 2)
        values = self.__board.get_value(0, 0)
        self.assertEqual(values, 2)

    def test_set_value(self):
        self.__board.set_value(0, 0, 2)
        self.assertEqual(self.__board.get_value(0, 0), 2)

    def test_is_valid(self):
        self.__board.set_value(0, 0, 2)
        val = self.__board.is_valid(1)
        self.assertEqual(val, True)

    def test_get_lowest_point(self):
        self.__board.set_value(0, 0, 2)
        low = self.__board.get_lowest_point(0)
        self.assertEqual(low, 5)

    def test_is_winner(self):
        self.__board.set_value(0, 0, 2)
        winner = self.__board.is_winner(2)
        self.assertEqual(winner, None)

    def test_get_empty_cells(self):
        self.__board.set_value(0, 0, 2)
        self.assertEqual(self.__board.get_empty_cells(), [Cell(line=0, column=1, value=0.0), Cell(line=0, column=2, value=0.0),Cell(line=0, column=3, value=0.0),Cell(line=0, column=4, value=0.0),Cell(line=0, column=5, value=0.0),
                                                          Cell(line=0, column=6, value=0.0),Cell(line=1, column=0, value=0.0),Cell(line=1, column=1, value=0.0),Cell(line=1, column=2, value=0.0),Cell(line=1, column=3, value=0.0),
                                                          Cell(line=1, column=4, value=0.0), Cell(line=1, column=5, value=0.0),Cell(line=1, column=6, value=0.0),Cell(line=2, column=0, value=0.0),Cell(line=2, column=1, value=0.0),
                                                          Cell(line=2, column=2, value=0.0), Cell(line=2, column=3, value=0.0), Cell(line=2, column=4, value=0.0),Cell(line=2, column=5, value=0.0),Cell(line=2, column=6, value=0.0),
                                                          Cell(line=3, column=0, value=0.0),Cell(line=3, column=1, value=0.0),Cell(line=3, column=2, value=0.0),Cell(line=3, column=3, value=0.0),Cell(line=3, column=4, value=0.0),
                                                          Cell(line=3, column=5, value=0.0),Cell(line=3, column=6, value=0.0),Cell(line=4, column=0, value=0.0),Cell(line=4, column=1, value=0.0),Cell(line=4, column=2, value=0.0),
                                                          Cell(line=4, column=3, value=0.0),Cell(line=4, column=4, value=0.0),Cell(line=4, column=5, value=0.0),Cell(line=4, column=6, value=0.0),Cell(line=5, column=0, value=0.0),
                                                          Cell(line=5, column=1, value=0.0),Cell(line=5, column=2, value=0.0),Cell(line=5, column=3, value=0.0),Cell(line=5, column=4, value=0.0),Cell(line=5, column=5, value=0.0),
                                                          Cell(line=5, column=6, value=0.0)])
    def test_get_all_cells(self):
        self.__board.set_value(0,0,2)
        self.assertEqual(self.__board.get_all_cells(), [Cell(line=0, column=0, value=2.0), Cell(line=0, column=1, value=0.0), Cell(line=0, column=2, value=0.0),Cell(line=0, column=3, value=0.0),Cell(line=0, column=4, value=0.0),Cell(line=0, column=5, value=0.0),
                                                          Cell(line=0, column=6, value=0.0),Cell(line=1, column=0, value=0.0),Cell(line=1, column=1, value=0.0),Cell(line=1, column=2, value=0.0),Cell(line=1, column=3, value=0.0),
                                                          Cell(line=1, column=4, value=0.0), Cell(line=1, column=5, value=0.0),Cell(line=1, column=6, value=0.0),Cell(line=2, column=0, value=0.0),Cell(line=2, column=1, value=0.0),
                                                          Cell(line=2, column=2, value=0.0), Cell(line=2, column=3, value=0.0), Cell(line=2, column=4, value=0.0),Cell(line=2, column=5, value=0.0),Cell(line=2, column=6, value=0.0),
                                                          Cell(line=3, column=0, value=0.0),Cell(line=3, column=1, value=0.0),Cell(line=3, column=2, value=0.0),Cell(line=3, column=3, value=0.0),Cell(line=3, column=4, value=0.0),
                                                          Cell(line=3, column=5, value=0.0),Cell(line=3, column=6, value=0.0),Cell(line=4, column=0, value=0.0),Cell(line=4, column=1, value=0.0),Cell(line=4, column=2, value=0.0),
                                                          Cell(line=4, column=3, value=0.0),Cell(line=4, column=4, value=0.0),Cell(line=4, column=5, value=0.0),Cell(line=4, column=6, value=0.0),Cell(line=5, column=0, value=0.0),
                                                          Cell(line=5, column=1, value=0.0),Cell(line=5, column=2, value=0.0),Cell(line=5, column=3, value=0.0),Cell(line=5, column=4, value=0.0),Cell(line=5, column=5, value=0.0),
                                                          Cell(line=5, column=6, value=0.0)])


if __name__ == '__main__':
    unittest.main()