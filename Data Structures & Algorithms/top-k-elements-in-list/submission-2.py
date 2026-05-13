class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = {}

        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in num_map.items():
            bucket[value].append(key)

        ans = []
        for value in bucket[::-1]:
            if k <= 0:
                break
            if len(value) == 0:
                continue
            
            ans.extend(value)

            if len(ans) == k:
                break

        return ans


        