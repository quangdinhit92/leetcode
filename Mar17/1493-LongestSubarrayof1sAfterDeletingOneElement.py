class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroLimit = 1
        n = len(nums)
        left = 0
        maxLen = 0
        for right in range(0, n):
            if 0 == nums[right]:
                zeroLimit -= 1
            while (
                zeroLimit < 0
            ):  # so phan tu vi pham luat vuot qua gioi han tuc la so phan tu =0 lon hon zeroLimit
                # di chuyen left de loai bo phan tu vi phan cu nhat, nue loai bo djuoc thi phuc hoi zeroLimit
                # co the phan tu dau tien la phan tu vi pham , nen kiem tra no trc
                if nums[left] == 0:
                    zeroLimit += 1
                left += 1
            maxLen = max(
                maxLen, right - left + 1 - 1
            )  # neu toan so 1 thi tru di 1, nguoc lai luon co 1 phan tu vi pham hoac k co phan tu nao

        return maxLen
