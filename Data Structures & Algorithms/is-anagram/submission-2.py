class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #str s and t are lowercase
        #First we check if s and t are the same length
        if len(s) != len(t):
            return False

        """
        Next we could create Hashmaps with the chars of
        str s and t as keys and the number of each char as the value.
        """

        hmapS = {}
        hmapT = {}
        for char in s:
            hmapS[char] = 0
        for char in t:
            hmapT[char] = 0

        for char in s:
            hmapS[char] += 1
        for char in t:
            hmapT[char] += 1

        """
        Then we check if str s has the same amount as str t
        """

        return hmapS == hmapT
