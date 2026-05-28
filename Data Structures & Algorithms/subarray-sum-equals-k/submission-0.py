class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0:1}
        currentsum = res = 0
        for num in nums:
            currentsum += num
            presum = currentsum - k
            res += prefixsum.get(presum, 0)
            prefixsum[currentsum] = prefixsum.get(currentsum, 0) + 1
        return res