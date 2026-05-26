from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        freq = [[] for i in range(len(nums)+ 1)]

        for key, val in s.items():
            freq[val].append(key)

        res = []
        
        for n in reversed(freq):
            for num in n:
                res.append(num)
                if len(res) == k:
                    return res

        
        
