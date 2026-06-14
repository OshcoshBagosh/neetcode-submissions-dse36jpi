class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_sub = 0
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_sub = max(max_sub, len(chars))

           
        return max_sub


