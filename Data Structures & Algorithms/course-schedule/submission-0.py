class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #[[0:1]]
        from collections import deque
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            in_degree[cur] += 1
        
        queue = deque()
        for course, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(course)
        count = 0
        while queue:
            node = queue.pop()
            count += 1
            for cur, pre in prerequisites:
                if node == pre:
                    in_degree[cur] -= 1
                    if in_degree[cur] == 0:
                        queue.append(cur)
        
        return count >= numCourses




        