class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #All prerequisite pairs are unique, 0 <= prerequisites.length <= 1000
        from collections import deque, defaultdict

        in_degree = [0] * numCourses
        order = []
        adj_list = defaultdict(list)

        for course, pre in prerequisites:
            in_degree[course] += 1
            adj_list[pre].append(course)

        queue = deque()
        for course, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for course in adj_list[node]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        if len(order) >= numCourses:
            return order
        else:
            return []
        
        