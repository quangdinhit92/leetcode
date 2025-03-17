class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        zeroLimit = k
        maxLen = 0
        for right in range(0, n):
            if nums[right] == 0:
                zeroLimit -= 1

            # right da gap so phan tu co gi tri 0 > k
            # di chuyen left tuyen tinh cho toi khi no loai bo dc 1 phan tu 0 de k >=0
            while zeroLimit < 0:
                if 0 == nums[left]:
                    zeroLimit += 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
        return maxLen
