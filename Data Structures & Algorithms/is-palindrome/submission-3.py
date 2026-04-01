class Solution:
    def isPalindrome(self, s: str) -> bool:
        #returns bool
        #skips chars that are not alnum
        #Is not case-sensative

        """
        We can use 2 pointers right and left to check if the both
        chars are the same.
        
        we will use a while loop 
        left starts at index 0 and right at len -1

        before comparing if a char is not alnum right or left will 
        move to the next index char

        when comparing, lowercase the left and right chars
        if they are the same continue if not return false

        when left index is greater than right index the while
        loop ends and returns true
        """

        left = 0
        right = len(s) - 1
        print(left)
        print(right)

        while (left < right):
            while(not s[left].isalnum()):
                if(left >= len(s)-1):
                    break
                left += 1
                print(f"left: {left}")

            while(not s[right].isalnum()):
                if(right <= 0):
                    break
                right -= 1
                print(f"Right: {right}")
            
            if(s[left].lower() != s[right].lower() and s[left].isalnum() and s[right].isalnum()):
                return False

            left += 1
            right -= 1
        return True
        