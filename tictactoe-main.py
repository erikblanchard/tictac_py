# -*- coding: utf-8 -*-

import numpy as np
from collections import Counter


def play_round(player, board, s, win_size):
    print('\n--------------------------------')
    print(f"Turn {turn} :: {symbol[player]}'s move")
    print('--------------------------------\n')
    while True:
        print_board(board, s)
        try:
            move = int(input("Your move:")) - 1
            if move not in range(0, s ** 2):
                raise ValueError
            if int(board[move // s, move % s]) != 0:
                raise LookupError
        except ValueError:
            print(f'Your input was invalid, please try again. Must be an integer within range of 1 and {s ** 2}')
        except LookupError:
            print('That space was already picked, please choose another number')
        else:
            board[move // s, move % s] = player
            win_check_temp = win_check(player, win_size, get_rcd(s, board, win_size))
            if win_check_temp == 'Win':
                print_end(f'{symbol[player]} wins!', board, s)
                return False
            elif win_check_temp == 'Tie':
                print_end('Tied game, no more moves!', board, s)
                return False
            else:
                return True


def get_rcd(s, board, win_size):
    """
    Parameters
    ----------
    s : int
         number that acts as the main parameter for calculating the two axes of the game board.
    board : numpy array
        Allows for parsing possible win-cases
    win_size : int
        win condition, ie how many contiguous spaces a player needs to win.

    Returns
    -------
    rcd : list
    Row Columns Diagonals, list of all possible axes that could meet win condition
    """

    # rows, columns, diagonals: for win condition
    rcd = []
    for ii in range(s):
        rcd.append(board[:, ii].tolist())
        rcd.append(board[ii].tolist())
        for i in range(s):
            rcd.append(np.diag(board, k=i).tolist())
            rcd.append(np.diag(np.fliplr(board), k=i).tolist())
            if i > 0:
                rcd.append(np.diag(board, k=-i).tolist())
                rcd.append(np.diag(np.fliplr(board), k=-i).tolist())
    for lst in rcd:
        if len(lst) > win_size:
            for i, item in enumerate(lst):
                if i + win_size <= s + 1:
                    rcd.append(lst[i:i + win_size])

    # list comprehension to omit any axis list that is not equal to win condition(win_size)
    rcd[:] = [lst for lst in rcd if not len(lst) < win_size] and [lst for lst in rcd if not len(lst) > win_size]

    return rcd


def win_check(player, win_size, rcd):
    tie_check = 0
    for lst in rcd:
        temp_collection = Counter(lst)
        if temp_collection.get(player) == win_size:
            return 'Win'
        elif temp_collection.get(0) is None:
            tie_check += 0
        else:
            tie_check += temp_collection.get(0)
    if tie_check == 0:
        return 'Tie'
    return 'None'


def print_board(board, s):
    """
    Parameters
    ----------
    board : numpy array
    s : int
        Board size, (s*s = board dimensions)

    Returns
    -------
    terminal printout of current game board.
    """
    padding = len(str(s ** 2))
    counter = 0
    for row in range(s):
        temp_string = "|"
        for i in board[row]:
            padding_mod = 1
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
                if padding_mod % 2 == 1:
                    temp_val = ' ' + temp_val
                    padding_mod += 1
                else:
                    temp_val = temp_val + ' '
                    padding_mod += 1
            temp_string += temp_val + "|"
        print(temp_string)


def print_end(message, board, s):
    """
    Parameters
    ----------
    message : string
        provided by function call, either game win message or tie.
    board : numpy array
    s : int

    Returns
    -------
    end message depending on board state, win vs tie.
    """
    print('\n')
    print_board(board, s)
    print('\n--------------------------------')
    print(message)
    print('--------------------------------\n')


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
        # Loop to establish board size. s*s = np.zeros array. Must be > 3
        try:
            s = int(input('Please enter board size: '))
            if s < 3:
                raise ValueError
            break
        except ValueError:
            print('Your input was invalid or too small, please use an integer')
    while True:
        # Loop to establish a valid win condition. Must be <= s and >= 1
        try:
            win_size = int(input('Please enter win condition: '))
            if win_size > s or win_size <= 1:
                raise ValueError
            break
        except ValueError:
            print(
                "Your input was invalid, please use an integer. "
                f"Make sure it's not larger than your selected board size: {s}")

    board = np.zeros((s, s))
    game_state = True

    # global vars
    global turn
    global symbol

    turn = 0
    symbol = {1: 'X', 2: 'O'}

    while game_state is True:
        turn += 1
        player = (turn % 2) + 1
        game_state = play_round(player, board, s, win_size)


game = True
game_number = 1

while game is True:
    print(f'Starting Game {game_number}!')
    main()
    while True:
        try:
            game_bool = input('Game over. Would you like to play again? Y/N: ')
            if game_bool.upper() in ['Y', 'YES']:
                game_number += 1
                game = True
                break
            elif game_bool.upper() in ['N', 'NO']:
                game = False
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid input, please type either Y for Yes, or N for No.')
