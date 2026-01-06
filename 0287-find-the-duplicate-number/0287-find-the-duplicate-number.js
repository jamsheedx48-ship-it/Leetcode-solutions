
var findDuplicate = function(nums) {
    nums.sort((a,b)=>{
        return a-b
    })


    let i=1
  for (x of nums){
   if(x===nums[i]){
     return x
   }
    i++
  }

    
};