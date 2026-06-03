class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a=word.upper()
        b=word.lower()
        c=word.capitalize()
       
        if word==a:
            return True
        elif word==b:
            return True
        elif word==c:
            return True
        else:
            return False