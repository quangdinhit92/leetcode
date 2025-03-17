class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxVal = float("-inf")
        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        for i in range(0, n - (k - 1)):
            if i == 0:
                maxVal = max(maxVal, prefixSum[k - 1])
            else:
                tmp = prefixSum[i + (k - 1)] - prefixSum[i - 1]
                maxVal = max(maxVal, tmp)

        return maxVal / k
