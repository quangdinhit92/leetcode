class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right =len(nums)
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
      
        # def bisecLeft(numbers:List[int],target,left,right):
        #     if left >=right:
        #         return left
        #     mid=(left+right)//2
        #     if numbers[mid]<target:
        #         return bisecLeft(numbers,target,mid+1,right)
        #     else:
        #         return bisecLeft(numbers,target,left,mid)
          
        
        # return bisecLeft(nums,target,0,len(nums))

