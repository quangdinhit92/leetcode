class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        st = []
        ans = [-1] * n
        myMap = {}
        for num2 in nums2:
            while st and num2 >= st[-1]:
                index = st.pop()
                myMap[index] = num2

            st.append(num2)
        for i, num1 in enumerate(nums1):
            ans[i] = myMap.get(num1, -1)
        return ans
