class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        a=nums[0]
        for i in range(1,len(nums)):
            if i%2!=0:
                a-=nums[i]
            if i%2==0:
                a+=nums[i]
        return a        
