#!/usr/bin/python3

import os

# We need to draw a board
def initialize_board():
	global board
	board = {
		'ul': ' ', 'uc': ' ', 'ur': ' ',
		'ml': ' ', 'mc': ' ', 'mr': ' ',
		'll': ' ', 'lc': ' ', 'lr': ' '
	}

# We need to show this board to the player
def display_board():
	os.system('clear')
	print('Current board is:')
	print(board['ul'] + '|' + board['uc'] + '|' + board['ur'])
	print('-----')
	print(board['ml'] + '|' + board['mc'] + '|' + board['mr'])
	print('-----')
	print(board['ll'] + '|' + board['lc'] + '|' + board['lr'])
	print()

# We need to ask the player's input
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
		invalid = validate_input(req_square)	

# We need to take that input and make sure that they're making an actual move.
def validate_input(i):
	valid_inputs = ('ul','uc','ur','ml','mc','mr','ll','lc','lr')
	if i in valid_inputs:
		return True
	else:
		return False

# We need to put that move on the board.
# We need to show this board to the player
# We need to confirm if win or draw. End game if so and state who won if anyone
# We need to determine a move. This is prioritized by: scoring a win, avoiding a loss, or a random move.
# We need to put that move on the board.
# We need to show this board to the player
# We need to confirm if win or draw.

initialize_board()
display_board()
request_move()
