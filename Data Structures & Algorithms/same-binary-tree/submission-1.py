# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def dfs(p, q):
            if not p and not q:
                return
            elif not p or not q:
                self.same = False
                return
            
            if p.val != q.val:
                self.same = False
                return
            
            if p.left and q.left:
                dfs(p.left, q.left)
            elif p.left or q.left:
                self.same = False
                return
            
            if p.right and q.right:
                dfs(p.right, q.right)
            elif p.right or q.right:
                self.same = False
                return

        dfs(p, q)
        return self.same