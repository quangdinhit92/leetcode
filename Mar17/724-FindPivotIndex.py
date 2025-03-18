class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * n
        suf = [0] * n
        pref[0] = nums[0]
        suf[len(nums) - 1] = nums[-1]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]
            suf[n - 1 - i] = suf[n - 1 - i + 1] + nums[n - 1 - i]

        for i in range(0, n):
            if pref[i] == suf[i]:
                return i
        return -1
