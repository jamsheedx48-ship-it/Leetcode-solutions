class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i

        a=num+1
        ans=[int(i) for i in str(a)]
        return ans