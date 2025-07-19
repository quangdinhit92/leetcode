class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check={}
        for i,num in enumerate(nums):
            if num not in check:
                check[num] =i
            else:
                if abs(check[num] -i) <=k:
                    return True
                else:
                    check[num] =i
        return False