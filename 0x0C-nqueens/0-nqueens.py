#!/usr/bin/python3
"""
Module to solve the N Queens Problem
"""


import sys

def argv_parse():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def nqueens(queens, diff, sum):
    p = len(queens)
    if p == n:
        queen_n.append(queens)
        return None
    for q in range(n):
        if q not in queens and p - q not in diff and p + q not in sum:
            nqueens(queens + [q], diff + [p - q], sum + [p + q])


if __name__ == "__main__":
    n = argv_parse()
    queen_n = []
    nqueens([], [], [])
    for row in range(len(queen_n)):
        queen_p = []
        for col in range(len(queen_n[row])):
            queen_p.append([col, queen_n[row][col]])
        print(queen_p)
