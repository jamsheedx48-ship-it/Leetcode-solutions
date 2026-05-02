class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        return len(set(a))==len(set(b))==len(set(zip(a,b)))
        