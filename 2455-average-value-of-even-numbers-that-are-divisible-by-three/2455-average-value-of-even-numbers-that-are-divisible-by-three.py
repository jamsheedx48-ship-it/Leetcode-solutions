class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            if i%2==0:
                if i%3==0:
                    s.append(i)
        
        summ=sum(s)
        count=len(s)
        if count==0:
            return 0
        ans=summ//count
        return ans
