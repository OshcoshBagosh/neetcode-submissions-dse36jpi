class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We could use the Counter data structure to get the frequency
        of each number

        Then we switch the key and values so its 
        {freq : list[numbers]}

        Next we go down from length of nums to 0 and add the most
        frequent numbers to the return list.
        """

        import collections

        count = Counter(nums)
        freq = {}

        for key, value in count.items():
            if(value not in freq):
                freq[value] = []
            freq[value].append(key)
        
        result = []
        i = len(nums)
        while k > 0:
            if(i in freq and len(freq[i]) != 0):
                result.append(freq[i].pop())
                k -= 1
            else:
                i -= 1
            
        print(freq)
        return result


        