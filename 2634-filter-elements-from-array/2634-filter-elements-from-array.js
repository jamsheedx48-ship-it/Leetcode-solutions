
var filter = function(arr, fn) {
    const a= arr.filter((curr,index)=>{
        return fn(curr,index)
    })

    return a
};