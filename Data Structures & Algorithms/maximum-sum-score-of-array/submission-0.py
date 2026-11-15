class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:

        n = len(nums)
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        for i in range(n-2, -1, -1):
            suffix.append(nums[i] + suffix[-1])

        return max(max(prefix), max(suffix))
        pass
