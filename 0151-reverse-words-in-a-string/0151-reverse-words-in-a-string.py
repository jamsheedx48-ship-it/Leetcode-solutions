class Solution:
    def reverseWords(self, s: str) -> str:
        lst=[]
        a=s.split()
        l=len(a)+1
        for i in range(1,l):
            lst.append(a[-i])

        d=" ".join(lst)
        ans=d.strip()
        return ans
        

            

        