from src.store import store

class Game:
    def __init__(self, board, player_one, player_two) -> None:
        self.board = board
        self.player_one = player_one
        self.player_two = player_two 
        self.id = len(store['games']) + 1


    # game actions
    # check winner
    # print board
    # change players turn
    # update board