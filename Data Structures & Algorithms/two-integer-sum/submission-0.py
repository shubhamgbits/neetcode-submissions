class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}
        result = []

        for index, value in enumerate(nums):

            if value in nums_map:
                result = [nums_map[value], index]
                break
            
            nums_map[target-value]= index
        
        return result

        