class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len (nums)
        theoricalSum =(n *(n+1)) //2
        return theoricalSum- sum(nums)         