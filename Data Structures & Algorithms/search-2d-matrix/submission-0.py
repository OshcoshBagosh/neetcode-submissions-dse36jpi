class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        lower, upper = 0, len(matrix) - 1
        while lower <= upper:
            middle = lower + ((upper - lower) // 2)
            print(middle)
            if matrix[middle][0] > target:
                upper = middle - 1
            elif matrix[middle][n] < target:
                lower = middle + 1
            else:
                res = self.search(matrix[middle], target)
                return res != None
        
        
        return False

    def search(self, nums: list[int], target: int):
        lower, upper = 0, len(nums)-1

        while lower <= upper:
            middle = lower + ((upper - lower) // 2)

            if nums[middle] < target:
                lower = middle + 1
            elif nums[middle] > target:
                upper = middle - 1
            else:
                return middle
            
        return None