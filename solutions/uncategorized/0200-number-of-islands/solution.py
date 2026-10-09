# 200. Number of Islands
# Problem: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
# Language: python3

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    islands += 1

                    queue = deque([(r, c)])
                    grid[r][c] = "0"   # mark visited when adding to queue

                    while queue:
                        cr, cc = queue.popleft()

                        directions = [
                            (1, 0),
                            (-1, 0),
                            (0, 1),
                            (0, -1)
                        ]

                        for dr, dc in directions:
                            nr = cr + dr
                            nc = cc + dc

                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == "1"):

                                grid[nr][nc] = "0"
                                queue.append((nr, nc))

        return islands