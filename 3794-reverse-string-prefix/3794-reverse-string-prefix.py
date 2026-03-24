class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        b=s[:k]
        c=b[::-1]
        d=c+s[k:]
        return d
        