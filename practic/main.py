from Domain.entities import Board
from Repository.repo import Game
from Console.ui import Console

if __name__ == '__main__':
    print(Board(3, 3).print_board())
    Repo = Game("Game.txt")
    console = Console(Repo)
    console.run_menu()
