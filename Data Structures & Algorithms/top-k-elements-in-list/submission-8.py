class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We could use the Counter data structure to get the frequency
        of each number

        Then we could use max heap to return the highest frequency
        numbers k times.
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


        