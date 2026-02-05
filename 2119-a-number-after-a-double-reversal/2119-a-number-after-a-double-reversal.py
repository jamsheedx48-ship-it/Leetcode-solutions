class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=str(num)
        b=a[::-1]
        rev1=int(b)
        c=str(rev1)
        d=c[::-1]
        rev2=int(d)

        if rev2==num:
            return True
        else:
            return False    
