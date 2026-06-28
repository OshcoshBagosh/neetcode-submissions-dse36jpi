class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        First we need a function that confirms whether a string is a palindrome
        or not
        Assumptions: since s contains only digits and English letters
        it can be case sensetive and no skipping whitespace

        First idea is to do a top down approach using recursion
        we split a string into 2 parts to find every possible substring
        s[:-1] and s[1:]
        ex)
                "ababd"
            "abab"      "babd"

        We return the biggest substring that is a valid palindrome
        if there is a valid palindrome we add it to cache (memoization)
        so we avoid repeating tasks
        """
        #determines if a str is a palindrome
        def is_palindrome(word: str):
            l, r = 0, len(word)-1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True
        #stores valid palindromes
        memo = {}
        def dfs(word):
            #checks if palindrome alr exisits
            if word in memo:
                return memo[word]
            #base case
            if word == "" or is_palindrome(word):
                #adds to cache
                memo[word] = word
                return word

            #splits str into 2
            w1, w2 = dfs(word[1:]), dfs(word[:-1])
            
            #picks the bigger substring
            biggest = w1 if len(w1) > len(w2) else w2

            #adds to cache
            memo[word] = biggest

            return biggest


        return dfs(s)
        