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
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result        