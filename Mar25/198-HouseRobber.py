class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, n):
            # trom nha i
            p = nums[i] + dp[i - 2]
            # kong trom nha i
            n = dp[i - 1]
            dp.append(max(p, n))
        print(dp)
        return max(dp)
