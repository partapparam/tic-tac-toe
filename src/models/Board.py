from src.models.Square import Square
from store import store


class Board:
    def __init__(self, game):
        self.board = {'TL': Square(), 'TM': Square(), 'TR': Square(),\
                      'ML': Square(), 'MM': Square(), 'MR': Square(),\
                        'BL': Square(), 'BM': Square(), 'BR': Square()}
        self.game_id = game.id
        self.id = len(store['boards']) + 1
        store['boards'][self.id] = self

    def print_board(self):
        print(f"{self.board['TL'].value} | {self.board['TM'].value} | {self.board['TR'].value}")
        print(f"{self.board['ML'].value} | {self.board['MM'].value} | {self.board['MR'].value}")
        print(f"{self.board['BL'].value} | {self.board['BM'].value} | {self.board['BR'].value}")

    def is_valid_move(self, position):
        return self.board[position].value == ''
            
    def update_board(self, position, player_tick):
        if not self.is_valid_move(position):
            print('This is not a valid move')
            return False
        self.board[position].value = player_tick
        return True
    # 
    # This will allow for expanding the board to have more squares
    # 
    # def make_board(self, rows, columns):
    #     board = []
    #     for i in range(0, columns):
    #         board.append([])
    #         for j in range(0, rows):
    #             board[i].append(Square())
    #     return board
    

    def winner(self):
        winning_options = [
            # Rows
            ['TL', 'TM', 'TR'],
            ['ML', 'MM', 'MR'],
            ['BL', 'BM', 'BR'],
            # columns
            ['TL', 'ML', 'BL'],
            ['TM', 'MM', 'BM'],
            ['TR', 'MR', 'BR'],
            # diagonal
            ['TL', 'MM', 'BR'],
            ['TR', 'MM', 'BL'],
            ]
        
        for a, b, c in winning_options:
            # Check each position value for match in winning options
            if self.board[a].value == self.board[b].value == self.board[c].value and self.board[a].value != '':
                # print('we have a winner')
                return self.board[a].value
        print('')
        return False
    