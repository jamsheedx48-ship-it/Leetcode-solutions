class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        c=0
        l=0
        r=1

        while r<len(s):
            if s[l]!=s[r]:
                c+=1
            l+=1
            r+=1    
        return c
       