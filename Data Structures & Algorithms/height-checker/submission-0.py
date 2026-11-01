class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        n = len(heights)

        for i in range(1, n):
            current = i
            left = i - 1

            while current > 0 and expected[left] > expected[current]:
                expected[left], expected[current] = expected[current], expected[left]
                current -= 1
                left = current - 1

        count = 0

        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        
        return count
        