class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = 3
        left = 0

        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                count += 1
        if sum(nums) != n:
            return -1
        return count
