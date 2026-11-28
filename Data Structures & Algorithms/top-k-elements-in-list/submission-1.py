import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq=Counter(nums)
        for count ,num in freq.items():
            # only add element if its more freq the ele at top of heap (lowest freq ele)
            if len(heap)==0 or heap[0][1]<count:
                heapq.heappush(heap,(count,num))
            # ensure we are not having more then k eles 
            if len(heap)>k:
                heapq.heappop(heap)
        return [ele[0] for ele in heap]
            
        
        