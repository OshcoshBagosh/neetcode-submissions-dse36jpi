class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #assume negative nums are included
        """
        We can start with a left and right pointer

        Since numbers in non decreasing order we can have left pointer
        at numbers[0] and right pointer at numbers[n-1]

        if left + right > target: right index -= 1
        if left + right < target: left index += 1
        if left + right = target: return indexes of pairs

        [1, 2, 3, 4, 5, 6, 7] target = 12
        [1, 3, 4, 4, 6, 8] target = 4
        """
        left = 0
        right = len(numbers) - 1
        
        while (left < right):
            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            elif total == target:
                return [left + 1, right + 1]

