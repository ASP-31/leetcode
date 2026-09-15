# 102. Binary Tree Level Order Traversal
# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Easy
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        