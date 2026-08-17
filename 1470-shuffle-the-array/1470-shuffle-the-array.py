class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=nums[:n]
        b=nums[n:]
        out=[]

        for i in range(n):
            out.append(a[i])
            out.append(b[i])

        return out

        