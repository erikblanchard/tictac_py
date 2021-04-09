# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:16:23 2021

@author: ErikB
"""
# board_size = 5


def board_columns(game_dict, board_size, board_size_sq):
    temp_column = []
    for column in range(board_size):
        list_temp=[]
        for i, num in enumerate(range(1, board_size_sq+1, board_size)):
            list_temp.append(game_dict[num+column]) 
        temp_column.append(list_temp)
    return temp_column

def board_rows(game_dict, board_size):
    temp_row = []
    for row in range(board_size):
        board_mod = row * board_size
        list_temp=[]
        for i, num in enumerate(range(1, board_size+1)):
            list_temp.append(game_dict[num+board_mod])
        temp_row.append(list_temp)
    return temp_row

def board_diagonals(game_dict, board_size):
    temp_diagonals = []
    numbuffer = 0
    temp_diag_one = []
    temp_diag_two = []
    while len(temp_diagonals) == 0:
        while len(temp_diag_one) != board_size:
            if len(temp_diag_one) == 0:
                numbuffer = 1
                temp_diag_one.append(game_dict[1])
            else:
                numbuffer += (board_size + 1)
                temp_diag_one.append(game_dict[numbuffer])
        temp_diagonals.append(temp_diag_one)
    while len(temp_diagonals) == 1:
        while len(temp_diag_two) != board_size:
            if len(temp_diag_two) == 0:
                numbuffer = board_size
                temp_diag_two.append(game_dict[board_size])
            else:
                numbuffer += (board_size - 1)
                temp_diag_two.append(game_dict[numbuffer])
        temp_diagonals.append(temp_diag_two)
    return temp_diagonals


def check_status(rows, columns, diagonals):
    for row in rows:
        if len(set(row)) == 1:
            return True
    for column in columns:
        if len(set(column)) == 1:
            return True
    for diagonal in diagonals:
        if len(set(diagonal)) == 1:
            return True


def update_rcd(game_dict, board_size, board_size_sq):       
    global rows, columns, diagonals
    rows = board_rows(game_dict, board_size)
    columns = board_columns(game_dict, board_size, board_size_sq)
    diagonals = board_diagonals(game_dict, board_size)
    
            
def start_game():
    print('Start game, please enter board size:')
    global board_size
    global board_size_sq
    board_size = int(input())
    board_size_sq = board_size ** 2
    X_win = board_size * 'X'
    O_win = board_size * 'O'
    global game_dict
    game_dict = {}
    
    for i in range(board_size_sq):
        game_dict.update({i+1:i+1})
    
    update_rcd(game_dict, board_size, board_size_sq)

    game_state = True  
    turn_tracker = 1
    while game_state == True:
        if turn_tracker % 2 == 0:
            marker = 'X'
        else:
            marker = 'O'
        print(f"It's {marker}'s turn!")
        play_round(marker)
        update_rcd(game_dict, board_size, board_size_sq)
        status = check_status(rows, columns, diagonals)
        if status == True:
            print_board(board_size)
            print(f"{marker} WINS!")
            game_state = False
        else:
            turn_tracker += 1

def print_board(board_size):
    current_board = list(game_dict.values())
    seq = 0
    print('\n')
    for i in range(board_size):
        row = '|'
        for e in range(board_size):
            row += str(current_board[i+e+seq]) + '|'
        seq += board_size - 1
        print (row)
    print('\n')
    
    
def play_round(marker):
    print_board(board_size)
    print('\n')
    _ = 0
    while _ == 0:
        move = int(input("Your move:"))
        while move in range(1,board_size_sq+1):
            if game_dict.get(move) == move:
                game_dict[move] = marker
                return None
            else:
                move = 'error'
                print('That square was alreaedy picked, or your input was invalid, please try again.')
                
start_game()
