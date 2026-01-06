
var isPowerOfTwo = function(n) {
   for(i=0;i<=1000;i++){
     if(n===Math.pow(2,i)){
        return true
     }
   }
   return false
};