# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.greater = max(p.val, q.val)
        self.lower = min(p.val, q.val)
    
        def dfs(curr):
            if not curr:
                return None
            if curr.val >= self.lower and curr.val <= self.greater:
                return curr
            elif curr.val < self.lower:
                return dfs(curr.right)
            else:
                return dfs(curr.left)
        
        return dfs(root)