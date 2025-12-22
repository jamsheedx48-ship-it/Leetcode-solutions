/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let a= String(x)
    let b = a.split("")
    let c= b.reverse()
    let d= c.join("")

    if(a===d){
        return true
    }else{
       return false
    } 
      
};