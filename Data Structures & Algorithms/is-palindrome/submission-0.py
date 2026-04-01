class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_1 = []

        for ch in s:
            if ch.isalnum():
                pal_1.append(ch.lower())

        pal_2 = []


        for i in range(len(pal_1) - 1, -1, -1):
            pal_2.append(pal_1[i])
            
        if pal_1 == pal_2:
            return True
        else:
            return False


        