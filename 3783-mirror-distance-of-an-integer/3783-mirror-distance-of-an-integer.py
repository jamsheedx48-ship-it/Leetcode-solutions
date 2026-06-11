class Solution:
    def mirrorDistance(self, n: int) -> int:
        a=str(n)
        b=a[::-1]
        return abs(int(a)-int(b))