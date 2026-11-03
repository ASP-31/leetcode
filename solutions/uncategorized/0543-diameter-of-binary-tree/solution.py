# 543. Diameter of Binary Tree
# Problem: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Language: python3

class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res