class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        First we need a function that confirms whether a string is a palindrome
        or not
        Assumptions: since s contains only digits and English letters
        it can be case sensetive and no skipping whitespace

        First idea is to do a top down approach using recursion
        we splu
        """
        count = 0
        res = ""
        def is_palindrome(word: str):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True
        
        memo = {}
        def dfs(word):
            nonlocal count
            if word in memo:
                return memo[word]
            if word == "" or is_palindrome(word):
                memo[word] = word
                return word
            
            w1, w2 = dfs(word[1:]), dfs(word[:-1])

            biggest = w1 if len(w1) > len(w2) else w2

            memo[word] = biggest

            return biggest


        return dfs(s)
        