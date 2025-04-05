class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:

            if nums1[m] < nums2[n]:
                nums1[l] = nums2[n]
                n -= 1
            else:
                nums1[l] = nums1[m]
                m -= 1
            l -= 1
        print(nums1)
        for i in range(m, -1, -1):
            nums1[l] = nums1[i]
            l -= 1
        for j in range(n, -1, -1):
            nums1[l] = nums2[j]
            l -= 1
        print(nums1)
