class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if 1 == numRows:
            return s

        rows = [[] for _ in range(numRows)]
        rIndex = 0
        direction = 1
        for ch in s:
            rows[rIndex].append(ch)
            if 0 == rIndex:
                direction = 1
            elif numRows - 1 == rIndex:
                direction = -1
            rIndex += direction

        ret = ""
        for row in rows:
            ret += "".join(row)
        return ret
