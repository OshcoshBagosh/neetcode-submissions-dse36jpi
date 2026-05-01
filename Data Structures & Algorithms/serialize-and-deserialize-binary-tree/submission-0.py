# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = []
        def dfs(node):
            if not node:
                self.s.append("N")
                return
            self.s.append(f"{node.val}")
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(self.s)
        return ",".join(self.s)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        self.i = 0
        
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(data[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
