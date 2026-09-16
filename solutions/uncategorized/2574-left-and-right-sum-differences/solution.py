# 2574. Left and Right Sum Differences
# Problem: https://leetcode.com/problems/left-and-right-sum-differences/
# Difficulty: Easy
# Language: python3

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left=0
        total=sum(nums)
        ans=[]
        for num in nums:
            
            right=total-left-num
            ans.append(abs(left-right))
            left+=num
        return ans
            