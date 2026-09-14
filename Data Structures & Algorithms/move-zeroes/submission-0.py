class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        ans_1 = []
      
        for i in range(len(nums)):
            if nums[i] == 0:
                ans.append(nums[i])
            else:
                ans_1.append(nums[i])

        nums[:] = ans_1 + ans