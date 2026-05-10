class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        for ana in strs:
            sorted_string = "".join(sorted(ana))

            if sorted_string not in map:
                map[sorted_string] = [ana]
            else:
                map[sorted_string].append(ana)

        return list(map.values())

        