class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        a=[]
        b=[]
        sum=0
        for i in s:
            if i in vowels:
                a.append(s.count(i))
            if i not in vowels:
                b.append(s.count(i))

        sum=max(a,default=0)+max(b,default=0)   
        return sum         


        