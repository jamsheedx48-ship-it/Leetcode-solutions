class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            ans=int(dividend/divisor)
            return ans-1

        ans=int(dividend/divisor)
        

        return ans
        