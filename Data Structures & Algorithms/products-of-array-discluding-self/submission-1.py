class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr=[0]*len(nums)
        if not nums:
            return prod_arr
        prefix_arr,suffix_arr=[0]*len(nums),[0]*len(nums)
        # print('prefix arr ', prefix_arr)
        prefix_arr[0]=nums[0]
        suffix_arr[len(nums)-1]=nums[len(nums)-1]
        # preifx build up
        for i in range(1,len(nums)):
            prefix_arr[i]=prefix_arr[i-1]*nums[i]
        # print('prefix arr',prefix_arr)
        # suffix build up
        for i in range(len(nums)-2,-1,-1):
            suffix_arr[i]=suffix_arr[i+1]*nums[i]
        # prodd arr build up
        # print('suffix_arr ',prefix_arr)
        prod_arr[0]=suffix_arr[1]
        prod_arr[len(nums)-1]=prefix_arr[len(nums)-2]
        for i in range(1,len(nums)-1):
            prod_arr[i]=prefix_arr[i-1]*suffix_arr[i+1]
        return prod_arr


        