from src.store import store


class Player:
    def __init__(self, name: str, tick: str) -> None:
        self.name = name
        self.tick = tick
        self.id = len(store['players']) + 1
        store['players'][self.id] = self

    def games(self):
        return [game for game in store['games'] if game.player_one \
                == self.id or game.player_two == self.id]
    
