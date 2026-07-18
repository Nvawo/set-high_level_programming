#!/usr/bin/python3
"""Solve the N Queens puzzle."""

import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col)."""
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n):
    """Solve the puzzle using backtracking."""
    if row == n:
        solution = []
        for r in range(n):
            solution.append([r, board[r]])
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


def main():
    """Validate arguments and start solving."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0, n)


if __name__ == "__main__":
    main()
