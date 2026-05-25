class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in res:
                return [res[val], i]
            res[nums[i]] = i


        