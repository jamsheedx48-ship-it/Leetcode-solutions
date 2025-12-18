
var searchInsert = function(nums, target) {
    nums.push(target)
    nums.sort(function(a, b){return a - b})
    const b= nums.find((curr)=>curr===target)
     const index=nums.indexOf(b);

     return index
};  