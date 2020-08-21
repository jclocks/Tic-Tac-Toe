#!/usr/bin/python3

import os

def initialize_board():
	global board
	board = {
		'ul': 'X', 'uc': 'X', 'ur': 'O',
		'ml': 'O', 'mc': 'O', 'mr': 'X',
		'll': 'X', 'lc': 'O', 'lr': ' '
	}

def display_board():
    os.system('clear')
    print('Current board is:')
    print(board['ul'] + '|' + board['uc'] + '|' + board['ur'])
    print('-----')
    print(board['ml'] + '|' + board['mc'] + '|' + board['mr'])
    print('-----')
    print(board['ll'] + '|' + board['lc'] + '|' + board['lr'])
    print()

# Prompt for input. If valid, mark board.
def request_move():
    print('Please input a square. You\'re playing as ' + player_choice + '. They are:')
    print('ul|uc|ur')
    print('--------')
    print('ml|mc|mr')
    print('--------')
    print('ll|lc|lr')

    proceed = False
    while proceed == False:
        req_square = input('Input a square: ')
        proceed = validate_input(req_square)	
    mark_board(req_square, player_choice)

# Confirm move is valid. Checks against position and if slot is empty.
def validate_input(i):
    valid_inputs = ['ul','uc','ur','ml','mc','mr','ll','lc','lr']
    if i in valid_inputs:
        if board[i] == " ":
            return True
        else:
            return False
    else:
        return False

# Take a position and a marker and mark the board appropriately.
def mark_board(var_space, player_marker):
    board[var_space] = player_marker

# Return True if X won, False if not.
def check_win_x():
    # Horizontals
    if board["ul"] == board["uc"] == board["ur"] == "X":
        return True
    elif board["ml"] == board["mc"] == board["mr"] == "X":
        return True
    elif board["ll"] == board["lc"] == board["lr"] == "X":
        return True
    # Verticals
    elif board["ul"] == board["ml"] == board["ll"] == "X":
        return True
    elif board["uc"] == board["mc"] == board["lc"] == "X":
        return True
    elif board["ur"] == board["mr"] == board["lr"] == "X":
        return True
    # Diags
    elif board["ul"] == board["mc"] == board["lr"] == "X":
        return True
    elif board["ll"] == board["mc"] == board["ur"] == "X":
        return True
    # No win
    else:
        return False

# Return True if O won, False if not.
def check_win_o():
    # Horizontals
    if board["ul"] == board["uc"] == board["ur"] == "O":
        return True
    elif board["ml"] == board["mc"] == board["mr"] == "O":
        return True
    elif board["ll"] == board["lc"] == board["lr"] == "O":
        return True
    # Verticals
    elif board["ul"] == board["ml"] == board["ll"] == "O":
        return True
    elif board["uc"] == board["mc"] == board["lc"] == "O":
        return True
    elif board["ur"] == board["mr"] == board["lr"] == "O":
        return True
    # Diags
    elif board["ul"] == board["mc"] == board["lr"] == "O":
        return True
    elif board["ll"] == board["mc"] == board["ur"] == "O":
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
