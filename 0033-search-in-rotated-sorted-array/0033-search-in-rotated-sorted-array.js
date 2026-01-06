/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
   if(nums.includes(target)){
      let a= nums.indexOf(target)
      return a
   } else{
     return -1
   }
};