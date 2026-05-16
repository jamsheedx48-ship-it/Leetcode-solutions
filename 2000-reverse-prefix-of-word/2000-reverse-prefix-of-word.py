class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a=word.index(ch)
            b=word[:a+1]
            rev=b[::-1]
            ans=rev+word[a+1:]
            return ans
        return word    