class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        We will first find a row that the target can be in by using binary search
        Once we find potential row,
        We use binary search for that specific row (list)
        if target is found return True
        else false
        """
        #length of n or each list
        n = len(matrix[0]) - 1
        lower, upper = 0, len(matrix) - 1
        #Find Possible row that contains target
        while lower <= upper:
            middle = lower + ((upper - lower) // 2)
            print(middle)
            #if left most num in curr list is greater than target then move upper down
            if matrix[middle][0] > target:
                upper = middle - 1
            #Vice-versa
            elif matrix[middle][n] < target:
                lower = middle + 1
            else:
                res = self.search(matrix[middle], target)
                return res != None
        
        
        return False
        
    #Binary Search helper function
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