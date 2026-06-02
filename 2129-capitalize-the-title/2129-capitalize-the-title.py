class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a=title.split(" ")
        c=[]
        for i in a:
            if 1<=len(i)<=2:
                c.append(i.lower())
            else:
                c.append(i.capitalize())
        
        b=" ".join(c)    
        return b