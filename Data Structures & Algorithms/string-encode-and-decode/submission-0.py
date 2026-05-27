class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            str_len = int(s[i:j])
            str_end = j + 1 + str_len
            res.append(s[j + 1: str_end])
            i = str_end
        return res
