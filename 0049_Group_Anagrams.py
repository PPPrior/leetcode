""" Hash Table """
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
