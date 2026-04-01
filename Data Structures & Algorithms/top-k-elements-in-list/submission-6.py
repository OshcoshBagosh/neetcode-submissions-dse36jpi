class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We could use the Counter data structure to get the frequency
        of each number

        Then we could use max heap to return the highest frequency
        numbers k times.
        """

        import collections

        largest = 0
        count = Counter(nums)
        freq = {}

        for key, value in count.items():
            if value > largest:
                largest = value
            if(value not in freq):
                freq[value] = []
            freq[value].append(key)
        result = []
        while k > 0:
            if(largest in freq and len(freq[largest]) != 0):
                result.append(freq[largest].pop())
                k -= 1
            else:
                largest -= 1
            
        print(freq)
        return result


        