# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:16:23 2021

Attemping to convert game board to use numpy array.

@author: ErikB
"""
# board_size = 5

import numpy as np
from collections import Counter

def main():
    
    print(
    '''
    Welcome to advanced tic-tac-toe!
    You will be asked to select two parameters for the game: board size and win condition.
    For board size: Input a single number that will act as both the X and Y axis of the board.
    ~~This number should not be smaller than 3!~~
    For win condition: Input a single number that represents how many contiguous spaces in a straight line you need to win.
    ~~This number should be no smaller than 2 and no larger than your selected board size!~~
    '''
    )

    while True:
        #Loop to establish boardsize. s*s = np.zeros array. Must be > 3
        try:
            s = int(input('Please enter board size: '))
            if s < 3:
                raise ValueError
            break
        except ValueError:
            print('Your input was invalid or too small, please use an integer')
    while True:
        #Loop to establish a valid win condition. Must be <= s and >= 1
        try:    
            win_size = int(input('Please enter win condition: '))
            if win_size > s or win_size <= 1:
                raise ValueError
            break
        except ValueError:
            print(f"Your input was invalid, please use an integer. Make sure it's not larger than your selected board size: {s}")
    
    board = np.zeros((s, s))
    game_state = True
    
    #global vars
    global turn
    global symbol
    
    turn = 0
    symbol = {1:'X',2:'O'}
    
    while game_state == True:    
        turn += 1
        player = (turn % 2) + 1
        game_state = play_round(player, board, s, win_size)
    
def play_round(player, board, s, win_size):
    print('\n--------------------------------')
    print(f"Turn {turn} :: {symbol[player]}'s move")
    print('--------------------------------\n')
    while True:
        print_board(board, s)
        try:
            move = int(input("Your move:")) - 1
            if move not in range(0,s**2):
                raise ValueError
            if int(board[move // s, move % s]) != 0:
                raise LookupError
        except ValueError:
            print(f'Your input was invalid, please try again. Must be an integer within range of 1 and {s**2}')
        except LookupError:
            print('That space was already picked, please choose another number')
        else:
            board[move // s, move % s] = player
            if win_check(player, board, s, win_size, get_rcd(s, board, win_size)) == True:
                print('\n')
                print_board(board, s)
                print('\n--------------------------------')
                print(f'{symbol[player]} wins!')
                print('--------------------------------\n')
                return False
            else:    
                return True

    
def get_rcd(s, board, win_size):
    '''
    Parameters
    ----------
    s : int
         number that acts as the main parameter for calculating the two axises of the game board.
    board : numpy array
        Allows for parsing possible win-cases
    win_size : int
        win condition, ie how many contiguous spaces a player needs to win.

    Returns
    -------
    vert : list
        List of all possible verticals that could ammount to a win-case.
        Function omits verticals that are either too large or too small.
    '''
    
    #rows, columns, diags: for win condition
    rcd = []
    for ii in range(s):
        rcd.append(board[:,ii].tolist())
        rcd.append(board[ii].tolist())
        for i in range(s):
            rcd.append(np.diag(board,k=i).tolist())
            rcd.append(np.diag(np.fliplr(board),k=i).tolist())
            if i > 0:    
                rcd.append(np.diag(board,k=-i).tolist())
                rcd.append(np.diag(np.fliplr(board),k=-i).tolist())
    for lst in rcd:
        if len(lst) > win_size:
            for i, item in enumerate(lst):
                if i + win_size <= s+1:
                    rcd.append(lst[i:i+win_size])
            
    rcd[:] = [lst for lst in rcd if not len(lst) < win_size] and [lst for lst in rcd if not len(lst) > win_size]

    return rcd

    
def win_check(player, board, s, win_size, rcd):

    for lst in rcd:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == win_size:
            return True
    return False

def print_board(board, s):
    '''
    Parameters
    ----------
    board_list : numpy 1D array
        lists all current values
    board_size : int
         number that acts as the main parameter for calculating the two axises of the game board.
    board_size_sq : int
        square of board_size, ie total number of spaces on board.

    Prints
    -------
    Prints out a console friendly read out of the up-to-date gameboard.
    '''
    padding = len(str(s ** 2))
    counter = 0
    for row in range(s):
        temp_string = "|"
        for i in board[row]:
            pmod = 1
            temp_i = str(int(i))
            temp_val = ''
            counter += 1
            if temp_i == '0':
                temp_val = str(counter)
            if temp_i == '1':
                temp_val = 'X'
            if temp_i == '2':
                temp_val = 'O'
            while len(temp_val) != padding:
                if pmod % 2 == 1:
                    temp_val = ' ' + temp_val
                    pmod += 1
                else:
                    temp_val = temp_val + ' '
                    pmod += 1
            temp_string += temp_val + "|"
        print(temp_string) 
        
main()
