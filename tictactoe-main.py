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
        try:
            s = int(input('Please enter board size: '))
            break
        except ValueError:
            print('Your input was invalid, please use an integer')
    board = np.zeros((s, s))
    #board_list = np.zeros(board_size_sq)
    # 0 is placeholder, 1 is X, 2 is O
    #board_list will track progress of the game and is used to print current board.
    #See win_check() for functions related to answer checking, which use board_list reshaped into a 2D array.
    game_state = True
    while True:
        try:    
            win_size = int(input('Please enter win condition: '))
            if win_size > s:
                raise ValueError
            if win_size <= 1:
                raise ValueError
            break
        except ValueError:
            print(f"Your input was invalid, please use an integer. Make sure it's not larger than your selected board size: {s}")
    
    turn = 0
    while game_state == True:    
        turn += 1
        player = (turn % 2) + 1
        game_state = play_round(player, turn, board, s, win_size)
    
def play_round(player, turn, board, s, win_size):
    if player == 1:
        symbol = 'X'
    else:
        symbol = 'O'
    print('--------------------------------')
    print(f"Turn {turn} :: {symbol}'s move")
    print('--------------------------------')
    print('\n')
    while True:
        print_board(board, s)
        move = None
        try:
            move = int(input("Your move:")) - 1
        except ValueError:
            print('Your input was invalid, please try again.')    
        print('\n')
        try:        
            while move in range(0, s ** 2):
                if int(board[move // s, move % s]) == 0 :
                    #board_list[move-1] = player
                    board[move // s, move % s] = player
                    if win_check(player, board, s, win_size) == True:
                        print_board(board, s)
                        print('--------------------------------')
                        print(f'{symbol} wins!')
                        print('--------------------------------')
                        print('\n')
                        return False
                    else:    
                        return True
                else:
                    raise ValueError
        except ValueError:
            print('That square was already picked, please choose another number')


    
def get_verticals(board_size, board_grid, win_size):
    '''
    Parameters
    ----------
    board_size : int
         number that acts as the main parameter for calculating the two axises of the game board.
    board_grid : numpy array
        Allows for parsing possible win-cases
    win_size : int
        win condition, ie how many contiguous spaces a player needs to win.

    Returns
    -------
    vert : list
        List of all possible verticals that could ammount to a win-case.
        Function omits verticals that are either too large or too small.
    '''
    vert = []
    for i in range(board_size):
        vert.append(board_grid[:,i].tolist())
    for lst in vert:
        if len(lst) > win_size:
            for i, item in enumerate(lst):
                if i + win_size <= board_size+1:
                    vert.append(lst[i:i+win_size])
    vert[:] = [lst for lst in vert if not len(lst) < win_size]
    vert[:] = [lst for lst in vert if not len(lst) > win_size]
    return vert
def get_horizontals(board_size, board_grid, win_size):    
    horz = []
    for i in range(board_size):
        horz.append(board_grid[i].tolist())
    for lst in horz:
        if len(lst) > win_size:
            for i, item in enumerate(lst):
                if i + win_size <= board_size+1:
                    horz.append(lst[i:i+win_size])
    horz[:] = [lst for lst in horz if not len(lst) < win_size]
    horz[:] = [lst for lst in horz if not len(lst) > win_size]
    return horz

def get_diagonals(board_size, board_grid, win_size):    
    diags = []
    for ii in range(board_size):
        for i in range(board_size):
            diags.append(np.diag(board_grid,k=i).tolist())
            diags.append(np.diag(np.fliplr(board_grid),k=i).tolist())
            if i > 0:    
                diags.append(np.diag(board_grid,k=-i).tolist())
                diags.append(np.diag(np.fliplr(board_grid),k=-i).tolist())
    for lst in diags:
        if len(lst) > win_size:
            for i, item in enumerate(lst):
                if i + win_size <= board_size+1:
                    diags.append(lst[i:i+win_size])
    diags[:] = [lst for lst in diags if not len(lst) < win_size]
    diags[:] = [lst for lst in diags if not len(lst) > win_size]
    return diags
    
         
    # print(vert)
    # print(horz)
    # print(diag)
    
def win_check(player, board, s, win_size):
    # global board_grid
    #board_grid = board_list.copy().reshape((board_size, board_size))
    
    vert = get_verticals(s, board, win_size)
    #print(vert)
    horz = get_horizontals(s, board, win_size)
    # print(horz)
    diags = get_diagonals(s, board, win_size)
    # print(diags)

    
    for lst in vert:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == win_size:
            return True
    for lst in horz:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == win_size:
            return True    
    for lst in diags:
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
    #board_grid = board_list.copy().reshape((board_size, board_size))
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
