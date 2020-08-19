#!/usr/bin/python3

import os

def initialize_board():
	global board
	board = {
		'ul': ' ', 'uc': ' ', 'ur': ' ',
		'ml': ' ', 'mc': ' ', 'mr': ' ',
		'll': 'X', 'lc': 'X', 'lr': 'X'
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
    print('Please input a square. You\'re playing as X. They are:')
    print('ul|uc|ur')
    print('--------')
    print('ml|mc|mr')
    print('--------')
    print('ll|lc|lr')

    proceed = False
    while proceed == False:
        req_square = input('Input a square: ')
        print('Debug: ' + req_square)
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
    if board["ul"] == "X" and board["uc"] == "X" and board["ur"] == "X":
        return True
    elif board["ml"] == "X" and board["mc"] == "X" and board["mr"] == "X":
        return True
    elif board["ll"] == "X" and board["lc"] == "X" and board["lr"] == "X":
        return True
    # Verticals
    elif board["ul"] == "X" and board["ml"] == "X" and board["ll"] == "X":
        return True
    elif board["uc"] == "X" and board["mc"] == "X" and board["lc"] == "X":
        return True
    elif board["ur"] == "X" and board["mr"] == "X" and board["lr"] == "X":
        return True
    # Diags
    elif board["ul"] == "X" and board["mc"] == "X" and board["lr"] == "X":
        return True
    elif board["ll"] == "X" and board["mc"] == "X" and board["ur"] == "X":
        return True
    # No win
    else:
        return False

# Return True if O won, False if not.
def check_win_o():
    # Horizontals
    if board["ul"] == "O" and board["uc"] == "O" and board["ur"] == "O":
        return True
    elif board["ml"] == "O" and board["mc"] == "O" and board["mr"] == "O":
        return True
    elif board["ll"] == "O" and board["lc"] == "O" and board["lr"] == "O":
        return True
    # Verticals
    elif board["ul"] == "O" and board["ml"] == "O" and board["ll"] == "O":
        return True
    elif board["uc"] == "O" and board["mc"] == "O" and board["lc"] == "O":
        return True
    elif board["ur"] == "O" and board["mr"] == "O" and board["lr"] == "O":
        return True
    # Diags
    elif board["ul"] == "O" and board["mc"] == "O" and board["lr"] == "O":
        return True
    elif board["ll"] == "O" and board["mc"] == "O" and board["ur"] == "O":
        return True
    # No win
    else:
        return False

# Select a game mode.
def initialize_game():
    global player_choice, opponent_type
    player_choice, opponent_type = "", ""
    while (player_choice != "X") and (player_choice != "O"):
        player_choice = input("Please choose X or O: ")
    while (opponent_type != "P") and (opponent_type != "C"):
        opponent_type = input("Please type P to play another human, or C for the computer: ")
    initialize_board()


initialize_game()
display_board()
request_move()
display_board()
check_win_debug = check_win_x()
print(str(check_win_debug))
