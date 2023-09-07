a = [1,2,3,4,5,6,6,7,7,8,87,4,8]

b = a.reduce((sum,e)=>{
    return sum+e
},0)

console.log(b)