class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums =    [1, 2, 4, 6]
        # prefix =  [1, 1, 2, 8]
        # suffix =  [48,24,6, 1]
        # ans =     [48, 24, 12, 8]
        prefix = [1]
        prefix_multiple = 1
        for i in range(1, len(nums)):
            prefix.append(prefix_multiple*nums[i-1])
            prefix_multiple*=nums[i-1]
        #return prefix
        suffix = [1]
        suffix_multiple = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix.insert(0, suffix_multiple*nums[i+1])
            suffix_multiple*=nums[i+1]
        #return suffix
        output = []
        for i in range(0, len(nums)):
            output.append(prefix[i] * suffix[i])
        
        return output
        