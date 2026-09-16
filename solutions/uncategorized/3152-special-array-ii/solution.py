# 3152. Special Array II
# Problem: https://leetcode.com/problems/special-array-ii/
# Difficulty: Medium
# Language: python3

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bad = [0] * len(nums)

        for i in range(1, len(nums)):
            bad[i] = bad[i - 1] + (nums[i] % 2 == nums[i - 1] % 2)

        ans = []

        for left, right in queries:
            ans.append(bad[right] == bad[left])

        return ans
