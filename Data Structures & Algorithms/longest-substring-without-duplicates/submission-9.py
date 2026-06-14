class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        max_sub = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_sub = max(max_sub,len(count))
            if count[s[r]] > 1:
                while count[s[r]] > 1:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        count.pop(s[l])
                    l += 1
        return max_sub

        """
        "zxyzxyz"
        l=z, r=z
        zxyz
        """


