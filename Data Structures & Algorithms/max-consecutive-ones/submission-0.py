class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0
        for i in nums:
            if i:
                l += 1
            else:
                res = max(res, l)
                l = 0
        return max(res, l)
