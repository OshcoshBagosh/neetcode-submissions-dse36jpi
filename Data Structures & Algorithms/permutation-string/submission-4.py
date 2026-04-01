class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if(len(s1) > len(s2)):
            return False

        size = len(s1)
        left = 0
        count1 = Counter(s1)
        window = Counter(s2[left: size])

        for right in range(size, len(s2) + 1):
            if count1 == window:
                return True
            if right < len(s2):
                window[s2[right]] = window.get(s2[right], 0) + 1 
            window[s2[left]] = window.get(s2[left], 0) - 1  
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1

        return False
        