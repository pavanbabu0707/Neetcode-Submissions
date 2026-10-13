class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(A, l, r):
            if r - l <= 1:
                return(A[l:r])

            if r - l > 1:
                mid = (l+r)//2

                L = mergesort(A, l, mid)
                R = mergesort(A, mid, r)

                return merge(L, R)
                
        def merge(L, R):

            result, i, j = [], 0, 0

            while i + j < len(L) + len(R):
                if i == len(L):
                    result.append(R[j])
                    j += 1
                elif j == len(R):
                    result.append(L[i])
                    i += 1
                elif L[i] <= R[j]:
                    result.append(L[i])
                    i += 1
                elif L[i] > R[j]:
                    result.append(R[j])
                    j += 1
            
            return result
        
        return mergesort(nums, 0, len(nums))
            

