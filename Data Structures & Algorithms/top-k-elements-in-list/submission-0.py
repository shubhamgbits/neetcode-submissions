class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = {}

        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)
        
        sorted_num_map = dict(
            sorted(
                num_map.items(), 
                key = lambda x : x[1],
                reverse = True
            ))

        ans = []
        for key in sorted_num_map:
            if k <= 0:
                break
            ans.append(key)
            k -= 1

        return ans


        