# 2483. Minimum Penalty for a Shop
# Problem: https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Difficulty: Medium
# Language: python3

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        right_y=customers.count('Y')
        left_n=0
        min_pen=right_y
        ans=0 #hour
        for i in range(len(customers)):
            if customers[i]=='Y':
                right_y-=1
            else:
                left_n+=1
            penalty=right_y+left_n
            if penalty<min_pen:
                min_pen=penalty
                ans=i+1
        return ans
        