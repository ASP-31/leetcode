# 51. N-Queens
# Problem: https://leetcode.com/problems/n-queens/
# Difficulty: Hard
# Language: python3

def placeQueens(i, cols, leftdiagonal, rightdiagonal, cur, result):
    n = len(cols)
    if i == n:
        # Build the required board format for LeetCode from the column indices
        board = []
        for col_idx in cur:
            row = ['.'] * n
            row[col_idx] = 'Q'
            board.append("".join(row))
        result.append(board)
        return
        
    for j in range(n):
        if cols[j] or rightdiagonal[i + j] or leftdiagonal[i - j + n - 1]:
            continue
            
        # Mark the cell occupied using numeric flags (0/1)
        cols[j] = 1
        leftdiagonal[i - j + n - 1] = 1
        rightdiagonal[i + j] = 1
        cur.append(j)  # Store 0-based column index
        
        placeQueens(i + 1, cols, leftdiagonal, rightdiagonal, cur, result)

        # Backtrack: remove the queen and reset flags to 0
        cur.pop()
        cols[j] = 0
        rightdiagonal[i + j] = 0
        leftdiagonal[i - j + n - 1] = 0

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = [0] * n
        leftdiagonal = [0] * (2 * n)
        rightdiagonal = [0] * (2 * n)
        cur = []
        result = []
        placeQueens(0, cols, leftdiagonal, rightdiagonal, cur, result)
        return result