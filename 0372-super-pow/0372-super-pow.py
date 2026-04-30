class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num=pow(a,int("".join(map(str,b))),1337)
        return num
        

    
        