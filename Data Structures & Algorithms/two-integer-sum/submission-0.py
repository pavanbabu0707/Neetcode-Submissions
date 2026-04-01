class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targ_pos = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in targ_pos:
                return[targ_pos[diff], i]
            targ_pos[nums[i]] = i


