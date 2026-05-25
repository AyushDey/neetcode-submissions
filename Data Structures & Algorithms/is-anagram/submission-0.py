class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for i in t:
            if i in s_dict:
                s_dict[i] -= 1
        
        return all(val == 0 for val in s_dict.values())
        
