# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        We can use bfs to travel layer by layer
        We swap the children then explore
        """
        from collections import deque
        queue = deque([root])

        while len(queue) > 0:
            node = queue.popleft()
            if node:
                temp = node.left
                # swap children
                node.left = node.right
                node.right = temp
                # add them to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
        