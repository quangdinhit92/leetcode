class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2,i3,i5=0,0,0
        ugli=[1]*n
        
        for i in range(1,n):
            
            next2=ugli[i2] * 2
            next3=ugli[i3] * 3
            next5=ugli[i5] * 5
            
            nextUgli = min(next2,next3,next5)
            
            ugli[i] =nextUgli

            if nextUgli == next2:
                i2+=1
            if nextUgli == next3:
                i3+=1
            if nextUgli == next5:
                i5+=1
        return ugli[-1]