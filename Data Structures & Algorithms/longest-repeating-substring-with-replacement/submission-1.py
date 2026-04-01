class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1 <= s.length <= 1000
        0 <= k <= s.length
        First we need to find most frequent char
        We can use a hashmapt/counter to keep track

        We use a sliding window that increases in size when there are spaces availible that can be change to
        most frequent char or are most frequent char.
        Decreases when number of replaced chars is > k
        replaced chars = window size - # of most freq char 
        Return largest substring length

        """
        count = {}
        res = 0

        left = 0
        maxfreq = 0
        for right in range(len(s)):
            #Increments frequency of char
            count[s[right]] = count.get(s[right], 0) + 1
            #Updates max freq char
            maxfreq = max(maxfreq, count[s[right]])
            
            #Subtract # of most frequent char to window size to get spaces replaced
            #if so decrease window size
            while (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            #Updates largest window size
            res = max(res, right - left + 1)

        return res

