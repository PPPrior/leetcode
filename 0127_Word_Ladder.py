""" Breadth-first Search """
from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordLen, ans = len(beginWord), 1
        queue1, visited1 = deque(), set()
        queue2, visited2 = deque(), set()
        queue1.append(beginWord)
        queue2.append(endWord)
        wordSet.remove(endWord)
        while queue1 and queue2:
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1
            n = len(queue1)
            for _ in range(n):
                word = queue1.popleft()
                for i in range(wordLen):
                    arr = list(word)
                    for j in range(26):
                        arr[i] = chr(97 + j)
                        nword = ''.join(arr)
                        if nword in queue2:
                            return ans + 1
                        if nword in wordSet and nword not in visited2:
                            queue1.append(nword)
                            visited2.add(nword)
            ans += 1
        return 0


print(Solution().ladderLength(
    beginWord="hot",
    endWord="dog",
    wordList=["hot", "dog"]
))
