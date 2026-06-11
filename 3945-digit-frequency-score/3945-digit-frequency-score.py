class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        a=str(n)
        b=list(a)
        c=[int(i) for i in b]
        
        d=reduce(lambda x,y:x+y,c)
        return d