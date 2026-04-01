class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []

        for i in nums:
            i = i**2
            arr.append(i)
        
        arr.sort()
        
        return arr