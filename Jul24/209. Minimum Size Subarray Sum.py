class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n= len(nums)
        prefix=[0]* (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+ nums[i]
        
        def bisect_left(arr,targ):
            left=0
            right =len(arr)
            while left<right:
                mid =(left+right)//2
                if arr[mid] < targ:
                    left=mid+1
                else:
                    right=mid
            return left
        min_len=float('inf')   
        for i in range(n):
            found = bisect_left(prefix,prefix[i]+ target)
            if found<=n:
                min_len=min(min_len,found-i)
        return 0 if min_len == float('inf') else min_len
                