from connect4.player.computer import Computer
from connect4.player.human import Human


class Game:
    def __init__(self, board, player1, player2):
        self.__board = board
        self.__player1 = player1
        self.__player2 = player2
        self.__last_move = None

    def play(self):
        while True:
            try:
                if self.__move(self.__player1, 1):
                    break
                if self.__move(self.__player2, 2):
                    break
            except ValueError as ve:
                print(ve)

    def __move(self, player, value):
        line, column = -1, -1
        if type(player) is Human:
            self.__draw_board()
            line, column = self.__read_data()
        self.__last_move = player.move(line, column, value)

        winner = self.__board.is_winner(value)
        if self.__is_over(self.__last_move) or winner:
            self.__show_game_over_status(player)
            return True
        return False

    def __read_data(self):
        column = int(input("Enter the column number: "))
        column = column - 1
        if column > 7:
            raise ValueError("Wrong column number.")

        line = self.__board.get_lowest_point(column)
        return line , column

    def __is_over(self, cell):
        if cell is None:
            return True
        if len(self.__board.get_empty_cells()) == 0:
            return True
        return False

    def __draw_board(self):
        print(self.__board)

    def __show_game_over_status(self, player):
        self.__draw_board()
        print("game over")
        if type(player) == Computer:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

    def __get_board_size(self):
        return self.__board.get_lines()

