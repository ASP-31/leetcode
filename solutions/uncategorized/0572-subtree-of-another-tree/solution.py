# 572. Subtree of Another Tree
# Problem: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        