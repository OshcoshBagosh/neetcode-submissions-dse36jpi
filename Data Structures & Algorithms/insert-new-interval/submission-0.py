class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        We have a list of intervals where intervals[i] = [start, end]
        they are sorted in ascending order

        we need to add a new interval to the mix.

        the output should not contain overlapping intervals if so merge them.

        how do we know when 2 intervals are overlapping?
        when interval1 end >= interval2 start

        if is_overlap(inter1,inter2)
        merge(inter1, inter2)
        else
        res.append(interval1)
        increment index

        to merge we want to out put a single combined interval. for start it should min(start1, start2)
        for end it should be max(end1, end2)
        """
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

        

