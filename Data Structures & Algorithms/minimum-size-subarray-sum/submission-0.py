class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, currsum = 0, 0
        res = float('inf')
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                res = min(res, r - l + 1)
                currsum -= nums[l]
                l += 1
        return 0 if res == float('inf') else res