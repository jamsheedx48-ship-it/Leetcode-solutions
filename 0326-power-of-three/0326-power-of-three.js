/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    for(i=0;i<=1000;i++){
        if(n===Math.pow(3,i)){
            return true
        }
    }
    return false
};