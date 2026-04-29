# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
        def dfs(curr, target):
            if not curr:
                return False
            if curr and curr.val == target:
                if isSameTree(curr, subRoot):
                    return True
            
            return dfs(curr.left, target) or dfs(curr.right, target)
        
        return dfs(root, subRoot.val)

        
        