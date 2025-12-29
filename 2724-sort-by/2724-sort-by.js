
var sortBy = function(arr, fn) {
    arr.sort((a,b)=>{
      const c = fn(a)-fn(b)
      return c
    })

    return arr
};