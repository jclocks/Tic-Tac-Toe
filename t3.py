#!/usr/bin/python3

import os

board = {
    'ul': ' ', 'uc': ' ', 'ur': ' ',
    'ml': ' ', 'mc': ' ', 'mr': ' ',
    'll': ' ', 'lc': ' ', 'lr': ' '
}

x_turn = True

def display_board():
    print('Current board is:')
    print(board['ul'] + '|' + board['uc'] + '|' + board['ur'])
    print('-----')
    print(board['ml'] + '|' + board['mc'] + '|' + board['mr'])
    print('-----')
    print(board['ll'] + '|' + board['lc'] + '|' + board['lr'])
    print()

def display_help():
    print('The available squares are:')
    print('ul|uc|ur')
    print('--------')
    print('ml|mc|mr')
    print('--------')
    print('ll|lc|lr')
    print()

def move_validation(chosen_square):
    return True if (chosen_square in ['ul', 'uc', 'ur', 'ml', 'mc', 'mr', 'll', 'lc', 'lr']) and (board[chosen_square] == ' ') else False

def mark_board(chosen_square):
    global x_turn
    if x_turn == True:
        board[chosen_square] = 'X'
    else:
        board[chosen_square] = 'O'
    x_turn = not x_turn

def game_over():
    # Horizontals
    if board['ul'] == board['uc'] == board['ur'] == 'X':
        print('X wins!')
        return True
    elif board['ml'] == board['mc'] == board['mr'] == 'X':
        print('X wins!')
        return True
    elif board['ll'] == board['lc'] == board['lr'] == 'X':
        print('X wins!')
        return True
    elif board['ul'] == board['uc'] == board['ur'] == 'O':
        print('O wins!')
        return True
    elif board['ml'] == board['mc'] == board['mr'] == 'O':
        print('O wins!')
        return True
    elif board['ll'] == board['lc'] == board['lr'] == 'O':
        print('O wins!')
        return True
    # Verticals
    elif board['ul'] == board['ml'] == board['ll'] == 'X':
        print('X wins!')
        return True
    elif board['uc'] == board['mc'] == board['lc'] == 'X':
        print('X wins!')
        return True
    elif board['ur'] == board['mr'] == board['lr'] == 'X':
        print('X wins!')
        return True
    elif board['ul'] == board['ml'] == board['ll'] == 'O':
        print('O wins!')
        return True
    elif board['uc'] == board['mc'] == board['lc'] == 'O':
        print('O wins!')
        return True
    elif board['ur'] == board['mr'] == board['lr'] == 'O':
        print('O wins!')
        return True
    # Diagonals
    elif board['ul'] == board['mc'] == board['lr'] == 'X':
        print('X wins!')
        return True
    elif board['ll'] == board['mc'] == board['ur'] == 'X':
        print('X wins!')
        return True
    elif board['ul'] == board['mc'] == board['lr'] == 'O':
        print('O wins!')
        return True
    elif board['ll'] == board['mc'] == board['ur'] == 'O':
        print('O wins!')
        return True
    # Draw Game
    elif ' ' not in board.values():
        print('Draw game.')
        return True
    # Not Over
    else:
        return False

# Game logic:
while game_over() == False:
    # Clear the screen.
    os.system('clear')
    # State whose turn it is.
    if x_turn == True:
        print('It\'s currently X\'s turn.')
    else:
        print('It\'s currently O\'s turn.')
    print()
    # Display the board and help.
    display_board()
    display_help()
    # Prompt for a square until a valid one is given.
    move_valid = False
    while move_valid == False:
        player_choice = input('Please make a move from the above squares: ')
        move_valid = move_validation(player_choice)
    # Mark the board / flip turn.
    mark_board(player_choice)
    # Loop handles exiting if the game's over.