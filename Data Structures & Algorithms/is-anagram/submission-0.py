class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            False

        dict_s = {char: 0 for char in s}
        dict_t = {char: 0 for char in t}

        for char in s:
            dict_s[char] += 1

        for char in t:
            dict_t[char] += 1

        if (dict_s == dict_t):
            return True
        else:
            return False