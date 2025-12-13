
var differenceOfSums = function(n, m) {
 let num1=0;
 let num2=0;
 
 const arr1=[]
    const arr2=[]
    for(i=0;i<=n;i++){
        if(i%m!==0){
           arr1.push(i)
        }else if(i%m==0){
            arr2.push(i)
        }
    }
for(i=0;i<arr1.length;i++){
    num1+=arr1[i]
}
for(i=0;i<arr2.length;i++){
    num2+=arr2[i]
}
    return num1-num2
};