# 1552. Magnetic Force Between Two Balls
# Problem: https://leetcode.com/problems/magnetic-force-between-two-balls/
# Difficulty: Medium
# Language: python3

class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:

        def isPossible(position, mid, m):
            count = 1
            last = position[0]

            for pos in position[1:]:
                if pos - last >= mid:
                    count += 1
                    last = pos

                    if count == m:
                        return True

            return False

        position.sort()

        low = 0
        high = position[-1] - position[0]
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if isPossible(position, mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans