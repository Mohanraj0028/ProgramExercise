let a = [2,3,4,2,6,78,43,56]

let b = a.filter(isEven)

function isEven(a){
    return a%2==0
}

console.log(b)
