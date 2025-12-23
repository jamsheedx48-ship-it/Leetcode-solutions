
var reduce = function(nums, fn, init) {
    const a = nums.reduce((acc,curr,index)=>{
        return fn(acc,curr)
    },init)

    return a
};