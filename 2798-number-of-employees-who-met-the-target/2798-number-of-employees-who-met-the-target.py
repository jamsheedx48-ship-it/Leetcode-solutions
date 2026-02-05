class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        j=0
        for i in range(len(hours)):
            if hours[i]>=target:
                j+=1
        return j
        if target not in hours:
            return 0        

        