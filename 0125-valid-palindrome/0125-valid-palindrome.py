class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        l=[i for i in a if i.isalnum()]
        b="".join(l)
        c=b[::-1]
        if c==b:
            return True
        
        else:
            return False            
        