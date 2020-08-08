#!/usr/bin/env python
# coding: utf-8




import random


def welcoming():
    print("Welcome to my simple Tic Tac Toe game")
    board = [' ' for x in range(9)]
    print_board(board)


def insert_letter(letter, pos):
    if pos < 0 or pos > 8:
        print("Out of range place")
    else:
        if board[pos] == ' ':
            board[pos] = letter.upper()
        else:
            print(pos)
            print("sorry place already occupyied")
            while board[pos] != ' ':
                pos = int(
                    input("Please enter where to place {} : ".format(letter)))
            board[pos - 1] = letter.upper()


def print_board(board):
    for i in range(0, 8, 3):
        print('   |   |   ')
        print(' {} | {} | {} '.format(board[i], board[i + 1], board[i + 2]))
        print('   |   |   ')

        if i != 6:
            print('-----------')


def board_full(board):
    if board.count(' ') < 1:
        return False
    else:
        return True


def check_winner(board):
    if check_horizontal(board) != None:
        return check_horizontal(board)
    elif check_vertical(board) != None:
        return check_vertical(board)
    elif check_diagoal(board) != None:
        return check_diagoal(board)
    else:
        return None


def check_horizontal(board):
    for i in range(0, 8, 3):
        if (board[i] == 'X' and board[i + 1] == 'X' and board[i + 2] == 'X'):
            return 'X'
        if (board[i] == 'O' and board[i + 1] == 'O' and board[i + 2] == 'O'):
            print(i)
            return 'O'


def check_vertical(board):
    for i in range(0, 3):
        if (board[i] == 'X' and board[i + 3] == 'X' and board[i + 6] == 'X'):
            return 'X'
        if (board[i] == 'O' and board[i + 3] == 'O' and board[i + 6] == 'O'):
            print(i)
            return 'O'


def check_diagoal(board):
    if (board[0] == 'X' and board[4] == 'X' and board[8] == 'X'):
        return 'X'
    if (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 'X'
    if (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):
        print(i)
        return 'O'
    if (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        print(i)
        return 'O'


def ai_computer():
    possible_places = [x for x, letter in enumerate(board) if letter == ' ']

    for sol in ['O', 'X']:
        for i in possible_places:
            board_copy = board[:]
            board_copy[i] = sol

            if check_winner(board_copy) == sol:
                return i

    corners = []
    for i in possible_places:
        if i in [0, 2, 6, 8]:
            corners.append(i)
    if len(corners) > 0:
        return random.choice(corners)

    if 4 in possible_places:
        return 4

    edges = []
    for i in possible_places:
        if i in [1, 3, 5, 7]:
            edges.append(i)
    if len(edges) > 0:
        return random.choice(edges)


def main():
    #board = [' ' for x in range(9)]

    while board_full(board) and (check_winner(board) == None):
        x = int(input("Please enter where to place x : "))
        if x == 2020:
            print("Hello master")
            print("closing game")
            break
        insert_letter("x", x - 1)
        print_board(board)
        print("\n")

        if board_full(board) and (check_winner(board) == None):
            insert_letter("o", ai_computer())
            print_board(board)
            print("\n")

    if (x != 2020):
        if (check_winner(board) != None):
            print("\nThe Winner is {}".format(check_winner(board)))
        else:
            print("\nThe Game is a Tie")





welcoming()

while 1:
    replay = input('Do you want to play (y/n): ')
    if replay.lower() == 'y':
        board = [' ' for x in range(9)]
        main()
    else:
        break
    


    













