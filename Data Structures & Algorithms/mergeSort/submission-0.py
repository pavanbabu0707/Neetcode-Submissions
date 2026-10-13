# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs

        mid = len(pairs)//2

        L = self.mergeSort(pairs[:mid])
        R = self.mergeSort(pairs[mid:])

        return self.merge(L, R)

    
    def merge(self, A, B):

        result = []
        m = len(A)
        n = len(B)

        i, j = 0, 0

        while i < m and j < n:

            if A[i].key <= B[j].key:
                result.append(A[i])
                i += 1

            else:
                result.append(B[j])
                j += 1

        result.extend(A[i:])
        result.extend(B[j:])

        return result

        