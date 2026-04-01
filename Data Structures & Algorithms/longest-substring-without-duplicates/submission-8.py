class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We can use a hashset to store uninque chars in str
        We iterate through str
        We have left and right pointers
        right pointer explores str for unique chars while increasing count
        if s[right] in hashset then left pointer increments till no duplicates in hash set
        """
        if s == "":
            return 0
        
        hs = set()
        left = 0
        hs.add(s[left])
        count = 1
        largest = 1

        for right in range(1, len(s)):
            if s[right] not in hs:
                hs.add(s[right])
                count = right - left + 1
            else:
                while(s[left] != s[right]):
                    hs.remove(s[left])
                    left += 1
                left += 1
                hs.add(s[left])
                count = right - left + 1

            if count > largest:
                    largest = count


        return largest
        