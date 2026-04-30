# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if node:
                    if i == l-1:
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return res

        