class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bai toan mo rong chuoi con voi dieu kien

        longest = 0

        left = 0
        check = set()
        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1
            check.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
