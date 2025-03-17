class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        checkNum = {}
        total = 0

        for num in nums:
            checkNum[num] = checkNum.get(num, 0) + 1

        for num in nums:
            left = k - num

            if left == num:
                pairs = checkNum[num]
                checkNum[num] -= pairs
                total += pairs // 2
            else:
                difPair = min(checkNum[num], checkNum.get(left, 0))

                total += difPair

                if 0 != difPair:
                    checkNum[num] -= difPair
                    checkNum[left] -= difPair

        return total
