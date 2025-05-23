class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            num = nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                total = num + nums[left] + nums[right]
                if 0 == total:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    if total < 0:
                        left += 1
                    else:
                        right -= 1
        return result
