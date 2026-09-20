# Split Array Largest Sum
# Problem: https://leetcode.com/problems/split-array-largest-sum/
# Difficulty: Medium
# Language: python3

class Solution:
    def isPossible(self,arr,k,mid):
        current_pages=0
        students=1
        for  book in arr:
            if current_pages+book <=mid:
                current_pages+=book
            else:
                students+=1
                current_pages=book
        return students<=k  
    def splitArray(self, arr: list[int], k: int) -> int:
        if k > len(arr):
            return -1
        low=max(arr)
        high=sum(arr)
        ans=0
        while low<=high:
            mid=low + (high-low)//2
            if self.isPossible(arr,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        