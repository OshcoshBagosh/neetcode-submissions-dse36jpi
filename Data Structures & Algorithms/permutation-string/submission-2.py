class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        size = len(s1)
        left = 0
        count1 = Counter(s1)

        if len(s1) == len(s2):
            return count1 == Counter(s2)

        for right in range(size, len(s2) + 1):
            count2 = Counter(s2[left: right])
            if count1 == count2:
                return True
            left += 1

        return False
        