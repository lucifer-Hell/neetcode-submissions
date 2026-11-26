class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map={}
        for idx , ele in enumerate(nums):
            if (target - ele) in idx_map:
                return [idx_map[target-ele],idx]
            idx_map[ele]=idx

        return []

