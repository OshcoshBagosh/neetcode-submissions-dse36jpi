class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #All prerequisite pairs are unique, 0 <= prerequisites.length <= 1000
        from collections import deque

        in_degree = [0] * numCourses
        order = []

        for course, pre in prerequisites:
            in_degree[course] += 1

        queue = deque()
        for course, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for course, pre in prerequisites:
                if node == pre:
                    in_degree[course] -= 1
                    if in_degree[course] == 0:
                        queue.append(course)

        if len(order) >= numCourses:
            return order
        else:
            return []
        
        