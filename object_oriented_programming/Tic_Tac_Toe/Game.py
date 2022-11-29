from .Board_of_Tic_Tac_Toe import Board
from TicTacToeClass import TacToePlayer


class Game:
    def __init__(self) -> None:
        self.game_board = Board()
        self.player_one = TacToePlayer("player 1", "X")
        self.player_two = TacToePlayer("player 2", "O")

    def create_player(self, name, sign):
        self.player_one = TacToePlayer(name, sign)

    def create_player_Two(self, name, sign):
        self.player_one = TacToePlayer(name, sign)

    def play(self, player: TacToePlayer, position: int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position, player.sign)

    def determine_winner(self):
        pass
