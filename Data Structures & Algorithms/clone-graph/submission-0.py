"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return None
        queue = deque([node])
        hm = {}
        while queue:
            curr = queue.popleft()
            hm[curr] = Node(curr.val)
            for n in curr.neighbors:
                if n not in hm:
                    queue.append(n)

        for key in hm.keys():
            for n in key.neighbors:
                hm[key].neighbors.append(hm[n])
            
                    
        return hm[node]
        