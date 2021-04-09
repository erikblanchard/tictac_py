# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:16:23 2021

Attemping to convert game board to use numpy array.

@author: ErikB
"""
# board_size = 5

import numpy as np
from collections import Counter


def start_game():
    global board_size
    global board_size_sq
    global board_list
    global winsize
    global turn
    
    #numpy conversion:
        # 0 is placeholder, 1 is X, 2 is O
        #board_list will track progress of the game and be used to print current board
    board_size = int(input('Please enter board size: '))
    board_size_sq = board_size ** 2  
    board_list = np.zeros(board_size_sq)
    game_state = True
    winsize = int(input('Please enter win condition: '))
    if winsize > board_size:
        winsize = board_size
        print(f'Win condition exceeded board size. Win condition is now {board_size}.')
    turn = 0
   
    while game_state == True:    
        turn += 1
        player = (turn % 2) + 1
        game_state = play_round(player)
    
def play_round(player):
    if player == 1:
        symbol = 'X'
    else:
        symbol = 'O'
    print_board()
    print('--------------------------------')
    print(f"Turn {turn} :: {symbol}'s move")
    print('--------------------------------')
    print('\n')
    looper = 0
    while looper == 0:
        move = int(input("Your move:"))
        print('\n')
        while move in range(1,board_size_sq+1):
            if int(board_list[move-1]) == 0 :
                board_list[move-1] = player
                if win_check(player) == True:
                    print_board()
                    print('--------------------------------')
                    print(f'{symbol} wins!')
                    print('--------------------------------')
                    print('\n')
                    return False
                else:    
                    return True
            else:
                move = 'error'
                print('That square was already picked, or your input was invalid, please try again.')



    
def get_verticals():  
    vert = []
    for i in range(board_size):
        vert.append(board_grid[:,i].tolist())
    for lst in vert:
        if len(lst) > winsize:
            for i, item in enumerate(lst):
                if i + winsize <= board_size+1:
                    vert.append(lst[i:i+winsize])
    vert[:] = [lst for lst in vert if not len(lst) < winsize]
    vert[:] = [lst for lst in vert if not len(lst) > winsize]
    return vert
def get_horizontals():    
    horz = []
    for i in range(board_size):
        horz.append(board_grid[i].tolist())
    for lst in horz:
        if len(lst) > winsize:
            for i, item in enumerate(lst):
                if i + winsize <= board_size+1:
                    horz.append(lst[i:i+winsize])
    horz[:] = [lst for lst in horz if not len(lst) < winsize]
    horz[:] = [lst for lst in horz if not len(lst) > winsize]
    return horz

def get_diagonals():    
    diags = []
    for ii in range(board_size):
        for i in range(board_size):
            diags.append(np.diag(board_grid,k=i).tolist())
            diags.append(np.diag(np.fliplr(board_grid),k=i).tolist())
            if i > 0:    
                diags.append(np.diag(board_grid,k=-i).tolist())
                diags.append(np.diag(np.fliplr(board_grid),k=-i).tolist())
    for lst in diags:
        if len(lst) > winsize:
            for i, item in enumerate(lst):
                if i + winsize <= board_size+1:
                    diags.append(lst[i:i+winsize])
    diags[:] = [lst for lst in diags if not len(lst) < winsize]
    diags[:] = [lst for lst in diags if not len(lst) > winsize]
    return diags
    
         
    # print(vert)
    # print(horz)
    # print(diag)
    
def win_check(player):
    global board_grid
    board_grid = board_list.copy().reshape((board_size, board_size))
    
    vert = get_verticals()
    print(vert)
    horz = get_horizontals()
    # print(horz)
    diags = get_diagonals()
    # print(diags)

    
    for lst in vert:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == winsize:
            return True
    for lst in horz:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == winsize:
            return True    
    for lst in diags:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == winsize:
            return True
    
    return False
    

def print_board():
    padding = len(str(board_size_sq))
    counter = 0
    board_grid = board_list.copy().reshape((board_size, board_size))
    for row in range(board_size):
        temp_string = "|"
        for i in board_grid[row]:
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
        
start_game()
