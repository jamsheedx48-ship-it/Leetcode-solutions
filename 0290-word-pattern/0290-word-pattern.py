class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split()
        return len(set(pattern))==len(set(a))==len(set(zip_longest(pattern,a)))
        