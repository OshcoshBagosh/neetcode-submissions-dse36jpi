class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        count = 0
        adj = defaultdict(list)
        visit = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                dfs(n, node)


        for i in range(n):
            if i in visit:
                continue
            count += 1
            dfs(i, -1)

        return count
        