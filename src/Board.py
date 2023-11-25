class Board:
    def __init__(self) -> None:
        # create a new board 
        # Each position in a board can be X, O or "" 
        self.board = {'TL': " ", "TM": " ", "TR": " ", 'ML': " ", "MM": " ", "MR": " ", 'BL': " ", "BM": " ", "BR": " "}
    
    def print_board(self):
        # print the board row by row
        print(self.board['TL'] + '|' + self.board['TM'] + '|' + self.board['TR'])
        print(self.board['ML'] + '|' + self.board['MM'] + '|' + self.board['MR'])
        print(self.board['BL'] + '|' + self.board['BM'] + '|' + self.board['BR'])

    def is_valid_move(self, position):
        if self.board[position] == ' ':
            return True 
        return False
    
    def change_board_after_move(self, position, player_type):
        # we are given a position on the board and the player type
        # check if the move is valid
        # modify board
        # print board
        if self.is_valid_move(position):
            self.board[position] = player_type
            return self.board
        else:
            print('this is not a valid move')
            return None
        
    def is_winner(self, player):
        """Returns True if the player won and False otherwise."""
        if self.board["TL"] == player.type and self.board["TM"] == player.type and self.board["TR"] == player.type or \
        self.board["ML"] == player.type and self.board["MM"] == player.type and self.board["MR"] == player.type or \
        self.board["BL"] == player.type and self.board["BM"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["ML"] == player.type and self.board["BL"] == player.type or \
        self.board["TM"] == player.type and self.board["MM"] == player.type and self.board["BM"] == player.type or \
        self.board["TR"] == player.type and self.board["MR"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["MM"] == player.type and self.board["BR"] == player.type or \
        self.board["BL"] == player.type and self.board["MM"] == player.type and self.board["TR"] == player.type:
            return True
        return False