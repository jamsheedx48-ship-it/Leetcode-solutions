class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            if nums.count(i)==1:
                a=i
        return a        
        