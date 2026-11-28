class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix,result=1,1,[0]*len(nums)
        # caluclate prefix
        for i in range(0,len(nums)):
            result[i]=prefix
            prefix*=nums[i]
        # print('prefix result ',result)
        # for last element the answer will be the complete product till i-1 
        # do run wwhile caluclating suffix
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*suffix
            suffix*=nums[i]
            # print('curr suffix ',suffix)
        # print('suffix ',suffix)
        return result