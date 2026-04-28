# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        max_num = 0
        if root:
            while stack:
                node, layer = stack.pop()
                max_num = max(max_num, layer)
                if node.right:
                    stack.append((node.right, layer + 1))
                if node.left:
                    stack.append((node.left, layer + 1))
        return max_num