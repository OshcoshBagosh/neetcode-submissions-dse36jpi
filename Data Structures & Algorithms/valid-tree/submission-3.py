class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        
        adj = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node: int, parent: int):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                if dfs(n, node) == False:
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n
        