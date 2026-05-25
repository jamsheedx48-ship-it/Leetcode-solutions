class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a=[]
        for i in matrix:
            a.append(sum(i))
        return a        

        