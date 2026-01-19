class Solution:
    import math
    def findGCD(self, nums: List[int]) -> int:
        a=math.gcd(min(nums),max(nums))
        return a
                     
