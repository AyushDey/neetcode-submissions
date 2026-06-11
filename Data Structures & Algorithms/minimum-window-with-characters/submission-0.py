class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) and s == "":
            return ""
        
        s_dict, t_dict = {}, {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        s_count, t_count = 0, len(t_dict)
        l = 0
        res, minlen = [], float('inf')
        for r, c in enumerate(s):
            s_dict[c] = s_dict.get(c, 0) + 1
            if c in t_dict and s_dict[c] == t_dict[c]:
                s_count += 1
            while s_count == t_count:
                diff = r - l + 1
                if diff < minlen:
                    res = [l,r]
                    minlen = diff
                s_dict[s[l]] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    s_count -= 1
                l += 1
        if minlen == float('inf'):
            return ""
        l, r = res
        return s[l: r + 1]
        
        