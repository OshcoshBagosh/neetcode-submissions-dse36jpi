class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find smallest substring in s that every char is in t including duplicates.
        we can keep track of frequency of chars with a Counter object (hashmap) as we
        use a sliding window finding a substring
        We will have a left and right pointer.
        right will explore until all chars in t are found otherwise return empty str
        if all chars found we update the smallest substring
        then left pointer will increment its index until it hits a char in t
        1 <= s.length <= 1000
        1 <= t.length <= 1000
        """
        from collections import Counter
        
        if not t or not s:
            return ""
        
        count_t = Counter(t)
        count_window = {}
        
        have, need = 0, len(count_t)
        res = ""
        minlen = 1001
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            count_window[char] = count_window.get(char, 0) + 1
            
            if char in count_t and count_window[char] == count_t[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < minlen:
                    minlen = right - left + 1
                    res = s[left:right + 1]
                
                count_window[s[left]] -= 1
                if s[left] in count_t and count_window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        return res