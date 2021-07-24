""" Hash Table """
from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d1 = defaultdict(lambda: defaultdict(int))
        d2 = set()
        ans = []
        for _, x, y in orders:
            d1[int(x)][y] += 1
            d2.add(y)
        d2 = sorted(d2)
        title = ["Table"]
        ans.append(title + d2)
        for idx in sorted(d1.keys()):
            temp = [str(idx)]
            for food in d2:
                temp.append(str(d1[idx][food]))
            ans.append(temp)
        return ans


print(Solution().displayTable(
    orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
