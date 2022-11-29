from .BoardException import BoardException


class Board:
    def __init__(self):
        self.board = [''] * 9

    @staticmethod
    def is_position_allowed(position):
        if position not in range(1, 10):
            raise BoardException("invalid cell position")

    def cell_is_Empty(self, position):
        self.is_position_allowed(position)
        return self.board[position - 1] == ''

    def is_board_full(self):
        return all(self.board)

    def fill_cell(self, position, sign) -> None:
        self.is_position_allowed(position)
        if self.cell_is_Empty(position):
            self.board[position - 1] = sign
        else:
            raise BoardException(f"Cell position{position} is not empty")

    def display(self):
        for index, cell in enumerate(self.board):
            if index != 0 and index % 3 == 0:
                print()
                if index != 0 and index % 3 == 0:
                    print("|", end="")
            print(f"{cell: ^3} |", end="")
            print()

        # if __name__ == '__main__':
        #     board = Board()
        #     print(board.board)
