# 875. Koko Eating Bananas
# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Language: python3

from typing import List

class Solution:
    
    # Function to check whether mid speed is enough
    # to eat all piles of bananas within k hours
    def check(self, arr, mid, k):
        totalHours = 0
        
         for i in range(len(arr)):
            totalHours += (arr[i] + mid - 1) // mid
        
        # Return True if required time is <= k
        return totalHours <= k

    def minEatingSpeed(self, arr: List[int], k: int) -> int:
        
        # Minimum possible speed
        lo = 1
        
        # Maximum possible speed
        hi = max(arr)
        
        res = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # Check if current speed works
            if self.check(arr, mid, k):

                # Try smaller speed
                res = mid
                hi = mid - 1
            else:
                # Increase speed
                lo = mid + 1

        return res