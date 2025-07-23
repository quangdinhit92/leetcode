class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(arr,target):
            l,r = 0,len(arr)
            while l<r:
                m= (l+r)//2
                if arr[m] < target:
                    l=m+1
                else:
                    r=m
            return l
        def bisect_right(arr,target):
            l,r = 0,len(arr)
            while l<r:
                m= (l+r)//2
                if arr[m] <= target:
                    l=m+1
                else:
                    r=m
            return l
        r1= bisect_left(nums,target)
        r2= bisect_right(nums,target)

        if r1==r2:
            return [-1,-1]
       
        return [r1,r2-1]