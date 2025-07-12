class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[1]
        for i in range(1,rowIndex+1):
            arr.append(0)
            for j in range(i,0,-1):
                arr[j]+=arr[j-1]
        return arr