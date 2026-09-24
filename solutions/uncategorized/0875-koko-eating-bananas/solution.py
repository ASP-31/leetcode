# 875. Koko Eating Bananas
# Problem: https://leetcode.com/problems/koko-eating-bananas/
# Difficulty: Medium
# Language: python3

def check(arr,mid,k):
    totalHours = 0
    for i in range(len(arr)):
        totalHours += (arr[i] + mid - 1) // mid

    # return true if required time is less than 
    # or equals to given hour, otherwise return false
    return totalHours <= k
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        
        res=high
        while low<=high:
            mid=low+ (high-low)//2
            if check(piles, mid, h):
                high = mid - 1
                res = mid
            else:
          
            # if cant finish bananas in given
            # hours, then increase the speed
                low = mid + 1
        return res