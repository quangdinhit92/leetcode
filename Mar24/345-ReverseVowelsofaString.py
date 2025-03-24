class Solution:
    def reverseVowels(self, s: str) -> str:

        n = len(s)
        ret = list(s)
        left = 0
        right = len(s) - 1
        vowels = ["a", "A", "e", "E", "i", "I", "u", "U", "o", "O"]

        while left <= right:
            while left < n and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1

            if left < n and right >= 0:
                ret[left] = s[right]
                ret[right] = s[left]
                left += 1
                right -= 1
        return "".join(ret)
