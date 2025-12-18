
var climbStairs = function(n) {
   
     if (n <= 3) {
    return n;
  }

  let prev = 2; // n = 2
  let current = 3; // n = 3
  let next;

  for (let i = 4; i <= n; i++) {
    next = prev + current;
    prev = current;
    current = next;
  }

  return current;

    
};