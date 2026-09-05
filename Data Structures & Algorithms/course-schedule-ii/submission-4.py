class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adj = defaultdict(list)
        in_degree = {}

        for i in range(numCourses):
             in_degree[i] = 0

        for cur, pre in prerequisites:
            in_degree[cur] = in_degree.get(cur, 0) + 1
            adj[pre].append(cur)

        from collections import deque

        q = deque()
        for k, v in in_degree.items():
            if v == 0:
                q.append(k)
        print(q)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            in_degree.pop(course)
            for c in adj[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        print(in_degree)
        if not in_degree:
            return res
        else:
            return []


