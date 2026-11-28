class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix,result=1,1,[0]*len(nums)
        for i in range(0,len(nums)):
            result[i]=prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*suffix
            suffix*=nums[i]
        return result