class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ''
        current_ch = S[0]
        compressed = ''
        count = 0
        for ch in S:
            if ch == current_ch:
                count += 1
            else:
                compressed += current_ch + str(count)
                current_ch = ch
                count = 1
        compressed += current_ch + str(count)
        return compressed if len(compressed) < len(S) else S


print(Solution().compressString(S="aabcccccaaa"))
