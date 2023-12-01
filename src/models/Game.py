from store import store
from src.models.Board import Board
from src.models.Player import Player

class Game:
    def __init__(self, name_one, name_two):
        self.id = (len(store['games']) + 1)
        store['games'][self.id] = self
        self.board = Board(self)
        self.player_one = Player(name_one, 'X')
        self.player_two = Player(name_two, 'O')

    def print_game_board(self):
        self.board.print_board()

    def check_winner(self):
        return self.board.winner()
        
    def change_turn(self, player):
        if player is self.player_one:
            return self.player_two
        else:
            return self.player_one

    def record_move(self, position, player_tick):
        # gets position and the player tick
        # updates board
        updated = self.board.update_board(position, player_tick)
        if not updated:
            print('Try again')
        return updated

