class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0
        for i in nums:
            if i:
                l += 1
                res = max(res, l)
            else:
                l = 0
        return res
