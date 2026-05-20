class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a=str(n)
        b=int(a[0])
        for i in range(1,len(a)):
            if i%2!=0:
                b-=int(a[i])
            else:
                b+=int(a[i])
        return b        


        