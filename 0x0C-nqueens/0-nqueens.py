#!/usr/bin/python3
"""
N queens algorithm
"""

import sys


def printSolution(board):
    """print the coordinates row and column for the position of
       each N queen in the posible solution
    Arg:
       - board: matrix[n][n], list of list
    """
    formatted_output = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                formatted_output.append([i, j])
    print(formatted_output)


def isSafe(board, row, col, n):
    """checking if a queen can be placed on board[row][col]
    Arg:
       - board: matrix[n][n], list of list
       - row: position i to check
       - col: position j to check
       - n: number of queens to placed
    Return: True or False
       - True: if the queen coulb be placed, save place
       - False: if there is not a save place
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, n):
    """
    Solves the N queen problem using Backtracking
    Arg:
       - board: list of list of size board[n][n] where n is the num of queens
       - col: check from column 0 until n and check if it's right to place
a queen there.
       - n: number of queens to be placed
    Return:
       - True: if all the queens are placed on the board
       - False: if a queen can not be placed
    """
    if col == n:
        printSolution(board)
        return True

    counter = False
    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            counter = solveNQUtil(board, col + 1, n) or counter
            board[i][col] = 0
    return counter


if __name__ == "__main__":
    """
    Take the arguments from the command line
    - nqueens N, where N is the number of queens to be placed
    """
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # initialized the board[n][n] depends on the getting number
    board = [[0 for i in range(n)] for j in range(n)]
    solveNQUtil(board, 0, n)
