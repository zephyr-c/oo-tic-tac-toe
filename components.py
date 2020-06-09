class Player():
    """A player of the tic-tac-toe game"""

    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece

class Move():
    """A single move in the tic-tac-toe game"""

    def __init__(self, author, position):
        self.author = author
        self.position = position

class Board():
    """Game Board containing/displaying the moves of the game"""

    def __init__(self):
        self.moves = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def display(self):
        for row in self.moves:
            print(' '.join(row))

    def add_move(self, player, location):
        space = self.moves[location[0]][location[1]]
        if space != '_':
            print('Space already occupied!\n Invalid move!')
        else:
            space = player.game_piece

class Game():
    """An instance of a game of tic-tac-toe"""

    def __init__(self, board, player1, player2, started_at, finished_at):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = started_at
        self.finished_at = finished_at
