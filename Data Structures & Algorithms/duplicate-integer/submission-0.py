class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for ele in nums:
            if ele not in freq:
                freq[ele]=0
            freq[ele]+=1
            if freq[ele]>1:
                return True
        return False
        