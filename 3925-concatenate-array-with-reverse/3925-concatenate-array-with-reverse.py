class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums[::-1]
        nums.extend(a)
        return nums
        