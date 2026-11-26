from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicate_set=set()
        for ele in nums:
            non_duplicate_set.add(ele)
        return len(nums)!=len(non_duplicate_set)