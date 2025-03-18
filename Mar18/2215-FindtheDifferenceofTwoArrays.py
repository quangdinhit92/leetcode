class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        for n in nums2:
            if n in set1:
                set1.remove(n)

        for m in nums1:
            if m in set2:
                set2.remove(m)

        return [list(set1), list(set2)]
