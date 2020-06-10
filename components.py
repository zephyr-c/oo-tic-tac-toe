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

    def __repr__(self):
        """display game piece in representation"""
        return f"{self.author.game_piece}"

class Board():
    """Game Board containing/displaying the moves of the game"""

    moves = [[' ', '1', '2', '3'], ['1', '_', '_', '_'], ['2', '_', '_', '_'], ['3', '_', '_', '_']]

    def display(self):
        for row in self.moves:
            print(row[0], row[1], row[2], row[3])

    def add_move(self, move):
        # space = self.moves[move.position[0]][move.position[1]]
        if self.moves[move.position[0]][move.position[1]] != '_':
            print('Space already occupied! \nInvalid move!')
        else:
            self.moves[move.position[0]][move.position[1]] = move

class Game():
    """An instance of a game of tic-tac-toe"""

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        # self.started_at = started_at
        # self.finished_at = finished_at

    # def check_winner(self):
    #     b = self.board.moves
    #     wins = {'d_right': [b[1][1], b[2][2], b[3][3]],
    #             'd_left': [b[3][1], b[2][2], b[1][3]],
    #             'col_1': [row[1] for row in b[1:]],
    #             'col_2': [row[2] for row in b[1:]],
    #             'col_3': [row[3] for row in b[1:]],
    #             'row_1': b[1],
    #             'row_2': b[2],
    #             'row_3': b[3]}
    #     for path in wins.values():
    #         if (all(spc(type) != str for spc in path) and
    #             all(spc.author == path[0].author for spc in path)):
    #             self.winner = path[0].author
    #             print(f"{self.winner} is the winner")
    #         else:
    #             print("No winner yet!")




if __name__ == '__main__':
    harry = Player("Harry", "X")
    hermione = Player("Hermione", "O")
    my_board = Board()
    game = Game(my_board, harry, hermione)
    first_move = Move(harry, [1, 3])
