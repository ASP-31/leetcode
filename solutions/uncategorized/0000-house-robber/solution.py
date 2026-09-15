# House Robber
# Problem: https://leetcode.com/problems/house-robber/
# Difficulty: Medium
# Language: python3

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        
        for num in nums:
            temp = curr
            curr = max(curr, prev + num)
            prev = temp
            
        return curr