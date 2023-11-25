from src.Board import *
from src.Game import *
from src.Player import *

def play():
    game = Game()
    game.print_valid_moves()
    player = game.player1
    num = 9
    while num > 0:
        num -= 1
        game.print_board()
        position = input(f'{player} its your turn')

        game.modify_board(position, player.type)

        if game.won_game(player):
            print(f'{player} is the winner')
        else:
            player = game.change_turn(player)
    
    if num == 0:
        print('Game over')

