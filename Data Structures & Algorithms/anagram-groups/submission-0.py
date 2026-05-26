from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            strs_dict[key].append(i)

        return list(strs_dict.values())
