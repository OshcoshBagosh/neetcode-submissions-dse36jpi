class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        largest = 0
        distance from index 0 and len(heights)
        distance = len(heights) - 1
        we can have a loop incrementing heights with having left and right pointers
        at max distance.
        we multiply distance * max height of left and right pointers
        if the product is > than largest then largest = product
        if heights[left] is less than heights[right]:
            left += 1
        else:
            right -= 1
        continue till loop is done
        return largest
        """

        largest = 0
        distance = len(heights) - 1
        left, right = 0, len(heights) - 1

        while(left < right):
            if(heights[left] < heights[right]):
                height = heights[left]
            else:
                height = heights[right]

            water = distance * height

            if (water > largest):
                largest = water
            
            if(heights[left] < heights[right]):
                left += 1
                distance -= 1
            else:
                right -= 1
                distance -= 1
        return largest
        