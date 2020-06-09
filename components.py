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

    moves = [[' ', '1', '2', '3'], ['1', '_', '_', '_'], ['2', '_', '_', '_'], ['3', '_', '_', '_']]

    def display(self):
        for row in self.moves:
            print(' '.join(row))

    def add_move(self, move):
        # space = self.moves[move.position[0]][move.position[1]]
        if self.moves[move.position[0]][move.position[1]] != '_':
            print('Space already occupied! \nInvalid move!')
        else:
            self.moves[move.position[0]][move.position[1]] = move.author.game_piece

class Game():
    """An instance of a game of tic-tac-toe"""

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        # self.started_at = started_at
        # self.finished_at = finished_at
