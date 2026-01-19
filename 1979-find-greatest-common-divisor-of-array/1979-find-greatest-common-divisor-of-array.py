class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mnd=set()
        mxd=set()
        nums.sort()
        mn=nums[0]
        mx=nums[-1]

        for i in range(1,mn+1):
            if mn%i==0:
                mnd.add(i)

        for j in range(1,mx+1):
            if mx%j==0:
                mxd.add(j) 

        common=mnd.intersection(mxd)
        res=max(common)

        return res             
