class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n_set = set()

        for num in nums:
            if num in n_set:
                return True
            
            n_set.add(num)

        return False