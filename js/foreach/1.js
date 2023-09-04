a = [1,2,3,4,5]
b = [6,7,8,9,10]
var sum1  = 0
a.forEach(element => {

    sum1 = sum1 + element
    
});

console.log("Sum of array a",sum1)
var sum2 = 0
b.forEach(e=>{
    sum2 = sum2+ e
})

console.log("Sum of array b",sum2)

console.log("total sum ",sum1+sum2)