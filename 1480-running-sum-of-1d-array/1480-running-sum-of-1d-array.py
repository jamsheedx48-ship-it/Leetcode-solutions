class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[nums[0]]

        for i in range(1,len(nums)):
            a.append(a[-1]+nums[i])

        return a

                
            