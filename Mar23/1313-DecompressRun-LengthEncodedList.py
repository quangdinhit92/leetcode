class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        tmp = []
        for i in range(0, len(nums) - 2 + 1, 2):
            (freq, val) = (nums[i], nums[i + 1])
            for fr in range(freq):
                tmp.append(val)
        return tmp
