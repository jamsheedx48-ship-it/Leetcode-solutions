class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=[i for i in nums if -10<i<10]
        double=[i for i in nums if 10<=abs(i)<=99]

        single_sum=sum(single)
        double_sum=sum(double)

        if single_sum!=double_sum:
            return True
        else:
            return False    


        