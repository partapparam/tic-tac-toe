from src.Player import Player
from src.Board import Board 

class Game:
    def __init__(self) -> None:
        # a game should have 2 players
        # define each player type
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.board = Board()

# print out valid moves
    def print_valid_moves(self):
        print("""
            TL - top left    | TM - top middle    | TR - top right
            ML - middle left | MM - center        | MR - middle right
            BL - bottom left | BM - bottom middle | BR - bottom right
              """)

    def print_board(self):
        self.board.print_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else: 
            return self.player1
        
    def won_game(self, player):
        return self.board.is_winner(player)

    def modify_board(self, position, type):
        # recieves position and player type
        # returns modified board if position was valid 
        # ask to try again otherwise 
        if self.board.change_board_after_move(position, type) is not None:
            return self.board.change_board_after_move(position, type)
        else:
            position = input('not available position, please try again')
            return self.board.change_board_after_move(position, type)
        
    