class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_table = [0]*26
        
        for i in range(len(s)):

            val_s = ord(s[i])
            val_t = ord(t[i])
            base = ord('a')
 
            hash_table[val_s-base] += 1
            hash_table[val_t-base] -= 1

        for value in hash_table:
            if value != 0:
                return False

        return True