class Solution:
    def scoreOfString(self, s: str) -> int:

        i = len(s) - 1
        total = 0

        for i in range(len(s) - 1):
            diff = abs(ord(s[i]) - ord(s[i +1]))
            total += diff

        return total

        