class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Khans Algo for topo sort
        from collections import deque
        #Find how many nodes are pointing to current
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            in_degree[cur] += 1
        
        #load courses with a degree of 0 to queue
        queue = deque()
        for course, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(course)

        count = 0
        #Use bfs
        while queue:
            node = queue.pop()
            count += 1
            #Find all courses that node leads to
            for cur, pre in prerequisites:
                if node == pre:
                    #decrement # of nodes pointing
                    in_degree[cur] -= 1
                    if in_degree[cur] == 0:
                        queue.append(cur)
        
        return count >= numCourses




        