class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        write = 0
        for i in range(0, n):
            if 0 != nums[i]:
                nums[write] = nums[i]
                write += 1
        for j in range(write, n):
            nums[j] = 0

        print(nums)
