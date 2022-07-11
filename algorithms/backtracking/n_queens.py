
from typing import List

solution = []


def isSafe(board: List[List[int]], row: int, column: int) -> bool:
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True


def solve(board: List[List[int]], row: int) -> bool:
    if row >= len(board):
        solution.append(board)
        printboard(board)
        print()
        return True


def printboard(board: List[List[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are: ", len(solution))
