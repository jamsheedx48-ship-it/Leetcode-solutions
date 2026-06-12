class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        a.sort()
        s="".join(a)
        b.sort()
        t="".join(b)
        print(a)
        print(b)
        if s==t:
            return True
        else:
            return False