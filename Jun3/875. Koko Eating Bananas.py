import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        left=1
        right=max(piles)

        def totalHour(speed:int):
            hours=0
            for pile in piles:
                hours +=math.ceil(pile/speed)
            return hours

        while left<right:
            mid =(left+right)//2
            if totalHour(mid)<=h:
                right=mid
            else:
                left=mid+1
        return right

            
