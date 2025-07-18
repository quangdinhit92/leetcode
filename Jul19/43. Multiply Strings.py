class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        
            
        for i in range(len(num1)):
            n1= 10*n1+int(num1[i])
        for i in range(len(num2)):
            n2=10*n2+int(num2[i])
        return str(n1*n2)