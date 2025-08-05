import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK =defaultdict(int)
        for num in nums:
            topK[num] +=1
        
       
        heap=[]
        for n,c in topK.items():
            if len(heap) <k:
                heapq.heappush(heap,(c,n))
            else:
                if heap[0][0] <c:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(c,n))
        return [v for _,v in heap]
        
       