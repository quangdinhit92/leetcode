# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2

            tmpResult = guess(mid)
            if 0 == tmpResult:
                return mid
            elif tmpResult > 0:
                left = mid + 1
            else:
                right = mid - 1
