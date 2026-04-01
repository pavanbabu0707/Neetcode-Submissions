class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        index_map = {}

        for i in range(len(nums2)): #Storing the index values of array 2
            index_map[nums2[i]] = i

        mappings = [0] * len(nums1)

        for i in range(len(nums1)):
            mappings[i] = index_map[nums1[i]]
        
        return mappings

        

        