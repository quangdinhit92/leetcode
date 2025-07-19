class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        setNum={"0","1","2","3","4","5","6","7","8","9"}
        s=s.strip()
        print(s)
        setSign={"+","-"}
        lenS = len(s)
        sign=1
        if 0 == lenS:
            return 0
            
        s0 =s[0] # only one char
        if 1 == lenS:
            if s0  in setNum:
                return int(s0)
            return 0
        
        total=0;
        if s0 not in setSign and s0 not in setNum:
            return 0

        if s0=="-":
            sign =-1
        elif s0 =="+":
            sign =1
    
        if s0 in setNum:
            total =int(s0)
 
        print(total)
        for ch in s[1:]:
            if ch in setNum:
                total=10 * total+int(ch)
            else:
                break
        result = sign * total
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result