/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    let a=[];
    for(i=1;i<=num-1;i++){
        if(num%i===0 ){
           a.push(i)
        }
    }

    const sum= a.reduce((acc,curr)=>{
          return acc+curr
    },0)

   if(sum===num){
    return true
   }
    return false
};