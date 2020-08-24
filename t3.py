#!/usr/bin/python3

import os

# Rework of board variable.
def initialize_board():
	global board
	board = "         "

def display_board():
    os.system('clear')
    print('Current board is:')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print()

# Prompt for input. If valid, mark board.
def request_move():
    print('Please input a square. You\'re playing as ' + player_choice + '. They are:')
    print('0|1|2')
    print('-----')
    print('3|4|5')
    print('--------')
    print('6|7|8')

    proceed = False
    while proceed == False:
        req_square = input('Input a square: ')
        proceed = validate_input(int(req_square))	
    mark_board(int(req_square), player_choice)

# Confirm move is valid. Checks against position and if slot is empty.
def validate_input(i):
    if (board[i] == " "):
        print(True)
        return True
    else:
        print(False)
        return False

# Take a position and a marker and mark the board appropriately.
def mark_board(var_space, player_marker):
    board[var_space] = player_marker

# Return True if X won, False if not.
def check_win_x():
    # Horizontals
    if board[0] == board[1] == board[2] == "X":
        return True
    elif board[3] == board[4] == board[5] == "X":
        return True
    elif board[6] == board[7] == board[8] == "X":
        return True
    # Verticals
    elif board[0] == board[3] == board[6] == "X":
        return True
    elif board[1] == board[4] == board[7] == "X":
        return True
    elif board[2] == board[5] == board[8] == "X":
        return True
    # Diags
    elif board[0] == board[4] == board[8] == "X":
        return True
    elif board[6] == board[4] == board[2] == "X":
        return True
    # No win
    else:
        return False

# Return True if O won, False if not.
def check_win_o():
    # Horizontals
    if board[0] == board[1] == board[2] == "O":
        return True
    elif board[3] == board[4] == board[5] == "O":
        return True
    elif board[6] == board[7] == board[8] == "O":
        return True
    # Verticals
    elif board[0] == board[3] == board[6] == "O":
        return True
    elif board[1] == board[4] == board[7] == "O":
        return True
    elif board[2] == board[5] == board[8] == "O":
        return True
    # Diags
    elif board[0] == board[4] == board[8] == "O":
        return True
    elif board[6] == board[4] == board[2] == "O":
        return True
    # No win
    else:
        return False

def check_draw():
    if ' ' not in board.values():
        return True
    else:
        return False

# Select a game mode.
def initialize_game():
    global player_choice, opponent_type
    player_choice, opponent_type = "", ""
    while (player_choice != "X") and (player_choice != "O"):
        player_choice = input("Please choose X or O: ")
        player_choice = player_choice.upper()
    while (opponent_type != "P") and (opponent_type != "C"):
        opponent_type = input("Please type P to play another human, or C for the computer: ")
        opponent_type = opponent_type.upper()
    initialize_board()

# Game flow
initialize_game()
game_over = False
while game_over == False:
    display_board()
    request_move()
    if (check_win_x() == True) or (check_win_o() == True) or (check_draw() == True):
        game_over = True
if check_win_x() == True:
    print("X wins!")
elif check_win_o() == True:
    print("O wins!")
else:
    print("Draw game!")
