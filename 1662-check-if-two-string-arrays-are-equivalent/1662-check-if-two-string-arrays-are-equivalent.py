class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        a=word1[0]
        for i in range(1,len(word1)):
            a+=word1[i]

        b=word2[0]
        for i in range(1,len(word2)):
            b+=word2[i]
        
        print(a)
        print(b)
        if a==b:
            return True
        else:
            return False

        
        