class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        freq = [[] for i in range(len(nums)+ 1)]
        for i in nums:
            s[i] = s.get(i, 0) + 1

        for key, val in s.items():
            freq[val].append(key)

        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        
        
