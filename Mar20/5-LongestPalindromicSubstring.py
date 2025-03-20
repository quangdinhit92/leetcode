class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n <= 1:
            return s
        ret = []

        for i in range(n):
            # chan
            left = i
            right = i + 1
            maxEven = ""
            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                maxEven = s[left] + maxEven + s[right]
                left -= 1
                right += 1

            # le
            left = i - 1
            right = i + 1
            maxOdd = s[i]

            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                maxOdd = s[left] + maxOdd + s[right]
                left -= 1
                right += 1

            if len(ret) < len(maxOdd):
                ret = maxOdd
            if len(ret) < len(maxEven):
                ret = maxEven

        return ret
