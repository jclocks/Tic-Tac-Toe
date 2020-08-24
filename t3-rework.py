#!/usr/bin/python3

import os

board = {
    'ul': ' ', 'uc': ' ', 'ur': ' ',
    'ml': ' ', 'mc': ' ', 'mr': ' ',
    'll': ' ', 'lc': ' ', 'lr': ' '
}

x_turn = True

def display_board():
    os.system('clear')
    print('Current board is:')
    print(board['ul'] + '|' + board['uc'] + '|' + board['ur'])
    print('--------')
    print(board['ml'] + '|' + board['mc'] + '|' + board['mr'])
    print('--------')
    print(board['ll'] + '|' + board['lc'] + '|' + board['lr'])
    print()

def display_help():
    print('Please input a square. You\'re playing as ' + player_choice + '. They are:')
    print('ul|uc|ur')
    print('--------')
    print('ml|mc|mr')
    print('--------')
    print('ll|lc|lr')
    print()

def move_validation(chosen_square):
    return True if (chosen_square in ['ul', 'uc', 'ur', 'ml', 'mc', 'mr', 'll', 'lc', 'lr']) and (board[chosen_square] == ' ') else False

def mark_board(chosen_square):
    if x_turn == True:
        board[chosen_square] = 'X'
    else:
        board[chosen_square] = 'O'
    x_turn = not x_turn

