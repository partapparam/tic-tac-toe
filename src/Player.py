class Player:
    # One player
    def __init__(self, type) -> None:
        # create a player and give them a type of move = X, O
        self.type = type 
    
    def __str__(self) -> str:
        return f'Player is of type = {self.type}'