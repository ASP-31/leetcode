# Move Zeroes
# Problem: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
# Language: python

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in nums:
            if i != 0:
                nums[count]=i
                count+=1
            
        while count < len(nums):
            nums[count]=0
            count+=1
