from src.store import store
from src.models.Square import Square

class Board:
    def __init__(self, rows = 0, columns = 0) -> None:
        pass

    def make_board(self, rows, columns):
        board = []
        for i in range(0, len(columns)):
            board.append([])
