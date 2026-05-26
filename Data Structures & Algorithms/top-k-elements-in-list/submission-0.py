class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            s[i] = s.get(i, 0) + 1
        sorted_s = dict(sorted(s.items(), key=lambda x: x[1], reverse=True))
        answer = list(sorted_s.keys())
        return answer[:k]