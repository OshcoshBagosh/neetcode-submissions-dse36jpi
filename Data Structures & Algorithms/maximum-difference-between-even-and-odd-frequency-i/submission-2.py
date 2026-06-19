class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        max_odd, min_even = 0, math.inf

        for key, val in freq.items():
            if val % 2 == 0:
                min_even = min(min_even, val)
            else:
                max_odd = max(max_odd, val)

        return max_odd - min_even
        