class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, maxC = 0, 0, 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxC = max(maxC, count[s[r]])
            if (r - l + 1) - maxC > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res