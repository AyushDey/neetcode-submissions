class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for val in nums_dict.values():
            if val > 1:
                return True
        return False