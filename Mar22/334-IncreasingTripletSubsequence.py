class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float("inf")
        second = float("inf")
        # tim so lon nhat dau tien -> first
        # sim so lon thu 2 dau tien ->second
        # tim so lon thu 3 -> ket qua True
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
