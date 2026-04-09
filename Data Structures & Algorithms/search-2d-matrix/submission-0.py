class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        low = 0
        high = m*n - 1

        while low <= high:
            mid_val = (low + high) // 2
            row = mid_val // n
            column = mid_val % n
            val = matrix[row][column]

            if target == val:
                return True
            elif val < target:
                low = mid_val + 1
            else:
                high = mid_val - 1

        return False


        
        