class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana_map = {}

        for word in strs:

            ht = [0]*26

            for char in word:
                ht[ord(char)-ord('a')] += 1

            tuple_ht = tuple(ht)

            if tuple_ht in ana_map.keys():
                ana_map[tuple_ht].append(word)

            else:
                ana_map[tuple_ht] = [word]
        
        return list(ana_map.values())
        