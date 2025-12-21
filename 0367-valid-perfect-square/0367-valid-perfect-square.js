/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    let a=Math.sqrt(num)
    let b= Math.floor(a)
    if(b*b===num){
        return true
    }
    return false
};