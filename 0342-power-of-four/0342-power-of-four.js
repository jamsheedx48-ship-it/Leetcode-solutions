/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    for(i=0;i<=1000;i++){
     let a= Math.pow(4,i)
     if(a===n){
        return true
     }
     

    }
    return false
};