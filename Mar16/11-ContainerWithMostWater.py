class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0

        left = 0
        right = len(height) - 1

        while left < right:
            tmp = min(height[left], height[right]) * (right - left)
            if tmp > ret:
                ret = tmp
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return ret
