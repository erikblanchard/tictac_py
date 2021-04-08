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
    
    # global pv
    
    #numpy conversion:
        # 0 is placeholder, 1 is X, 2 is O
        #board_main will track progress of the game
        #board_dict will provide visual printout
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
            
        
    # print(board_list)
    # print(board_grid)
    # print('test:')
    # print_board()
    
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
    return vert

def get_horizontals():    
    horz = []
    for i in range(board_size):
        horz.append(board_grid[i].tolist())
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
    return diags
    
        
    # print(vert)
    # print(horz)
    # print(diag)
    
def win_check(player):
    global board_grid
    board_grid = board_list.copy().reshape((board_size, board_size))
    
    vert = get_verticals()
    # print(vert)
    horz = get_horizontals()
    # print(horz)
    diags = get_diagonals()
    # print(diags)
    #This might be ultimately unneeded but gave me some practice implementing list comprehension
    #Iterates over diags to delete any diagonal set that could not hold a win condition, resulting in a cleaner list
    diags[:] = [lst for lst in diags if not len(lst) < winsize]
    
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


    # game_state = True  
    # turn_tracker = 1
    # while game_state == True:
    #     if turn_tracker % 2 == 0:
    #         marker = 'X'
    #     else:
    #         marker = 'O'
    #     print(f"It's {marker}'s turn!")
    #     play_round(marker)
    #     update_rcd()
    #     status = check_status()
    #     if status == True:
    #         print_board()
    #         print(f"{marker} WINS!")
    #         game_state = False
            
    #     else:
    #         turn_tracker += 1
    

                
# start_game()



# def board_columns():
#     temp_column = []
#     for column in range(board_size):
#         list_temp=[]
#         for i, num in enumerate(range(1, board_size_sq+1, board_size)):
#             list_temp.append(board_dict[num+column]) 
#         temp_column.append(list_temp)
#     return temp_column

# def board_rows():
#     temp_row = []
#     for row in range(board_size):
#         board_mod = row * board_size
#         list_temp=[]
#         for i, num in enumerate(range(1, board_size+1)):
#             list_temp.append(board_dict[num+board_mod])
#         temp_row.append(list_temp)
#     return temp_row

# def board_diagonals():
#     temp_diagonals = []
#     numbuffer = 0
#     temp_diag_one = []
#     temp_diag_two = []
#     while len(temp_diagonals) == 0:
#         while len(temp_diag_one) != board_size:
#             if len(temp_diag_one) == 0:
#                 numbuffer = 1
#                 temp_diag_one.append(board_dict[1])
#             else:
#                 numbuffer += (board_size + 1)
#                 temp_diag_one.append(board_dict[numbuffer])
#         temp_diagonals.append(temp_diag_one)
#     while len(temp_diagonals) == 1:
#         while len(temp_diag_two) != board_size:
#             if len(temp_diag_two) == 0:
#                 numbuffer = board_size
#                 temp_diag_two.append(board_dict[board_size])
#             else:
#                 numbuffer += (board_size - 1)
#                 temp_diag_two.append(board_dict[numbuffer])
#         temp_diagonals.append(temp_diag_two)
#     return temp_diagonals


# def check_status():
#     for row in rows:
#         if len(set(row)) == 1:
#             return True
#     for column in columns:
#         if len(set(column)) == 1:
#             return True
#     for diagonal in diagonals:
#         if len(set(diagonal)) == 1:
#             return True


# def update_rcd():       
#     global rows, columns, diagonals
#     rows = board_rows()
#     columns = board_columns()
#     diagonals = board_diagonals()
    
# def print_board():
#     current_board = list(board_dict.values())
#     seq = 0
#     #the padding value that we will check against and apply to our printed numbers
#     print('\n')
#     for i in range(board_size):
#         row = '|'
#         for e in range(board_size):
#             temp_string = str(current_board[i+e+seq])
#             pass_mod = 1
#             #modulo function that will loosely center the text, flipping whether the space goes before or after based on iterations
#             while len(temp_string) != pv:
#                 if pass_mod % 2 != 0:
#                     temp_string = ' '+temp_string
#                     pass_mod += 1
#                 else:
#                     temp_string = temp_string+' '
#                     pass_mod += 1
#             row += temp_string + '|'
#         seq += board_size - 1
#         print (row)
#     print('\n')