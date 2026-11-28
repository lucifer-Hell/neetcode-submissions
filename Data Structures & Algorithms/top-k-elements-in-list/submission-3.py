import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        freq=Counter(nums)
        for num ,count in freq.items():
            # print('curr heap ',heap)
            # only add element if its more freq the ele at top of heap (lowest freq ele)
            heapq.heappush(heap,(count,num))
            # ensure we are not having more then k eles 
            # print('after adding heap ',heap)
            if len(heap)>k:
                heapq.heappop(heap)
        # print('heap size ',len(heap))
        # print('heap ',heap)
        return [ele[1] for ele in heap]
            
        


