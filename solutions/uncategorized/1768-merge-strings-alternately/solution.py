# 1768. Merge Strings Alternately
# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Language: python3

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        list=[]
        while i <len(word1) and j <len(word2):
            list.append(word1[i])
            i+=1
            list.append(word2[j])
            j+=1
        list.append(word1[i::])
        list.append(word2[j::])
        return "".join(list)   