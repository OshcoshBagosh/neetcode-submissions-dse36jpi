class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs = set()
        for num in nums:
            if not num in hs:
                hs.add(num)
            else:
                return num