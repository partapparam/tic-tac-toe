from src.models.Game import Game

def start_game():
    name_one = input('Player X - choose name:  ')
    name_two = input('Player O - enter name:  ')
    game = Game(name_one = name_one, name_two= name_two)
    current_player = game.player_one
    i = 0
    while not game.check_winner():
        i += 1
        print('')
        game.print_game_board()
        position = input(f'{current_player.name} its your turn:  ')

        move_saved = game.record_move(position, current_player.tick)
    # ensure that  the move is valid, else we should ask for another turn
        if move_saved == False:
            i -= 1
            # we essentially go again
        else:  
            current_player = game.change_turn(current_player)
    print('game over. Winner is: ', game.check_winner())
    if i == 9:
        print('game over -- We have a tie')


