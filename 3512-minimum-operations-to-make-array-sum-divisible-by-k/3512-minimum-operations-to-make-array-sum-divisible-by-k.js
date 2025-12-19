
var minOperations = function(nums, k) {
    const sum=nums.reduce((acc,curr)=> acc+=curr,0)
    return sum%k
};