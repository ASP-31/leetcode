# 2485. Find the Pivot Integer
# Problem: https://leetcode.com/problems/find-the-pivot-integer/
# Difficulty: Easy
# Language: python3

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = n * (n + 1) // 2

        for i in range(1, n + 1):
            left += i
            right -= i - 1

            if left == right:
                return i

        return -1
