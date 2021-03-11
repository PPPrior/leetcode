""" String """


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        curRow, isDown = 0, -1
        for ch in s:
            rows[curRow] += ch
            if curRow == 0 or curRow == numRows - 1:
                isDown = -isDown
            curRow += isDown
        return "".join(rows)


print(Solution().convert(s="PAYPALISHIRING", numRows=4))
