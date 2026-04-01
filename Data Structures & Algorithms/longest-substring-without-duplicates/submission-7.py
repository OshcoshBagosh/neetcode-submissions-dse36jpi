class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We can use a hashset to store uninque chars in str
        We iterate through str
        if char is not in set
        then the char is added to the set and increment count
        if char is in the set, we break the loop and return count
        """
        if s == "":
            return 0
        
        hs = set()
        left = 0
        hs.add(s[left])
        count = 1
        largest = 1
        #set= {a} count = 1 l = 1
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
        