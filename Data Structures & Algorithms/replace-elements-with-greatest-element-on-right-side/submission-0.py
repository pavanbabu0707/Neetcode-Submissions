class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        new_arr = []
        n = len(arr)

        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i+1] < arr[j]:
                    arr[i+1] = arr[j]

            new_arr.append(arr[i+1])
        
        new_arr.append(-1)
            
        return new_arr
        