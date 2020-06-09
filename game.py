from components import *

print("Welcome to tic-tac-toe!")
p1_name = input('Player 1 name: ')
p1_piece = input('X or O?: ')
p2_name = input('Player2 name: ')
if p1_piece == 'X':
    p2_piece = 'O'
else:
    p2_piece = 'X'
print(f"Player 2 will be {p2_piece}")

player1 = Player(p1_name, p1_piece)
player2 = Player(p2_name, p2_piece)
game_board = Board()
game_board.display()

def turn(player, board):
    print(f"{player.name}'s turn")
    row = input("Enter a row number: ")
    column = input("Enter a column number: ")
    move = Move(player, [int(row), int(column)])

    board.add_move(move)
    board.display()

moves_made = 0

while moves_made <= 9:
    turn(player1, game_board)
    moves_made += 1
    turn(player2, game_board)
    moves_made += 1
