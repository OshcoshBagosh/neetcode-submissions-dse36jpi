# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque([(root, 1)])
        max_num = 0

        if root:
            while queue:
                node, layer = queue.popleft()
                max_num = max(max_num, layer)
                
                if node.left:
                    queue.append((node.left, layer + 1))
                if node.right:
                    queue.append((node.right, layer + 1))
        return max_num
