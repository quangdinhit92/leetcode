class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        maxVal = 0

        check = {"a", "e", "i", "o", "u"}

        for i in range(0, k):
            if s[i] in check:
                maxVal += 1

        ret = maxVal
        for i in range(k, n):

            if s[i] in check:
                maxVal += 1
            if s[i - k] in check:
                maxVal -= 1

            ret = max(maxVal, ret)

        return ret
