class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0
        
        ans = left = 0
        curr = 1

        for i in range(len(nums)):
            curr = curr * nums[i]

            while curr >= k:
                curr = curr//nums[left]
                left += 1

            ans = ans + i - left + 1

        return ans