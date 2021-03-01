""" Sliding Window """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = n = 0
        while j < len(s):
            if s[j] in s[i:j]:
                i += 1
            else:
                j += 1
                n = max(n, j - i)
        return n


print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
