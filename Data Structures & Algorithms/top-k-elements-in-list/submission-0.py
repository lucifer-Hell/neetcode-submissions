from collections import defaultdict
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict=defaultdict(int)
        for ele in nums:
            freq_dict[ele]+=1
        sorted_list= sorted(freq_dict.items(),key=lambda key: key[1],reverse=True)
        return [sorted_list[i][0] for i in range(min(k,len(sorted_list)))]

        