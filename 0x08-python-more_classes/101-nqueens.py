#!/usr/bin/python3
'''program that solves the N queens problem.'''
import sys


def in_board(n):
    '''An n x n sized chessboard with 0's.'''
    board = []
    [board.append([]) for num in range(n)]
    [row.append(' ') for num in range(n) for row in board]
    return (board)


def copy(board):
    '''Return copy of a chessboard'''
    if isinstance(board, list):
        return list(map(copy, board))
    return (board)


def get_sol(board):
    '''Returns the list of lists representation of a solved chessboard.'''
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                solution.append([i, j])
                break
    return (solution)


def x_out(board, row, col):
    '''x_out spots on a chessboard.
    Args:
        board (list): Current working chessboard
        row (int): The row where  queen was played last
        col (int): Column where a queen was last played
    '''
    # x_out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # x_out all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # x_out of all sports below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # x_out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # x_out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x_out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # x_out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x_out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recur_solve(board, row, queens, sols):
    '''Recursive solution of an N-queens puzzle

    Args:
        board (list): Current working chessboard.
        row (int): Current working Row.
        queens (int): Current number of placed queens.
        sols (int): List of lists of solutions.
    '''
    if queens == len(board):
        sols.append(get_sol(board))
        return (sols)

    for c in range(len(board)):
        if board[row][c] == " ":
            board_temp = copy(board)
            board_temp[row][c] = "Q"
            x_out(board_temp, row, c)
            sols = recur_solve(board_temp, row + 1, queens + 1, sols)
    return (sols)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = in_board(int(sys.argv[1]))
    sols = recur_solve(board, 0, 0, [])
    for sol in sols:
        print(sol)
