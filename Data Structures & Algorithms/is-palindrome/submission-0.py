class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "".join([char.lower() for char in s if char.isalnum()])
        reverseString = "".join([char for char in reversed(newString)])

        if (reverseString == newString):
            return True
        else:
            return False 