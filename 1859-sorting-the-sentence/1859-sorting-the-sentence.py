class Solution:
    def sortSentence(self, s: str) -> str:
        ar=[]
        a=s.split(" ")
        a.sort(key=lambda x:x[-1])
        b=[i[:-1] for i in a]
        ans=" ".join(b)
        return ans
        

        
            
        