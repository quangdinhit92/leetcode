class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
       
        
        def sumk(nums,start,k,target):
            n=len(nums)
            res=[]
            if k ==2:
                left=start
                right = len(nums)-1
                while left<right:
                    total = nums[left] + nums[right]
                    if target == total:
                        res.append([nums[left],nums[right]])
                        left+=1
                        right -=1

                        while left<right and nums[left] == nums[left-1]:
                            left+=1
                        while left<right and nums[right] == nums[right+1]:
                            right -=1
                  
                    elif total <target:
                        left+=1
                    else:
                        right-=1
       
                return res
           
            for i in range(start, n - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # ✅ Fix: proper pruning using actual value estimates
                if nums[i] + (k - 1) * nums[i + 1] > target:
                    break
                if nums[i] + (k - 1) * nums[-1] < target:
                    continue

                for subset in sumk(nums, i + 1, k - 1, target - nums[i]):
                    res.append([nums[i]] + subset)
            
            return res
      
        return sumk(nums,0,4,target)