/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    nums.sort((a,b)=>{
        return a-b
    })
    let a=1
    for (x of nums){
        if(x===a){
            a++
        }
    }
    return a
};