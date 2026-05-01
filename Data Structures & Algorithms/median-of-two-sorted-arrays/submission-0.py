class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)

        ls = []
        for num in nums1:
            ls.append(num)
        for num in nums2:
            ls.append(num)
        
        ls.sort()

        if n % 2 == 0:
            mid = n // 2
            print(mid)
            return (ls[mid] + ls[mid - 1]) / 2
        else:
            return math.ceil(ls[n//2])