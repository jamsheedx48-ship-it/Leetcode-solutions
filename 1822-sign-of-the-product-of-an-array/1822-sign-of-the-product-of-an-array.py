class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a=reduce(lambda x,y:x*y,nums)
        if a<0:
            return -1
        elif a==0:
            return 0
        elif a>0:
            return 1        
        