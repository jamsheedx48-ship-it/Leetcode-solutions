class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        ls=list(s)
        a=[i for i in s if i in vowels]
        b=a[::-1]

        vi=0
        for i in range(len(ls)):
            if ls[i] in vowels:
                ls[i]=b[vi]
                vi+=1
        return "".join(ls)         
