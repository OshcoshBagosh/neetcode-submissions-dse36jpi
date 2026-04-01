class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1 <= s.length <= 1000
        0 <= k <= s.length
        First we need to find most frequent char
        We can use a hashmapt/counter to keep track

        We use a sliding window that increases in size when there are spaces availible that can be change to
        most frequent char or are most frequent char.
        Decreases when number of replaced strs is > k
        Return largest substring

        """
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res