class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        if sum(nums) == n:
            return n - 1
        totalMax = 0
        zeroCount = 1
        left = 0
        for right in range(0, len(nums)):

            if 0 == nums[right]:
                zeroCount -= 1

            while zeroCount < 0:
                if nums[left] == 0:
                    zeroCount += 1
                left += 1

            totalMax = max(totalMax, right - left)

        return totalMax
