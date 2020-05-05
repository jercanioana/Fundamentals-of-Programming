from connect4.board.board import Board
from connect4.game import Game
from connect4.player.computer import Computer
from connect4.player.human import Human
from connect4.strategy.no_strategy import NoStrategy
from connect4.strategy.strategy import Strategy



if __name__ == '__main__':
    board = Board()
    strategy = NoStrategy()
    player1 = Computer(1, board, strategy)
    player2 = Human(2, board)
    game = Game(board, player1, player2)

    game.play()