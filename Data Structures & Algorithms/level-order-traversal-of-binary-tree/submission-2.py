# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque([root])

        while queue:
            ls = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    ls.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if ls:
                res.append(ls)

        return res
        