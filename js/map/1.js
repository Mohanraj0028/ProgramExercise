a = [1,2,3,4,5]

b = a.map(e => e*e)

console.log(b)

console.log("Funtion")


c = a.map(square)

function square(a){

    a = a*a
    return a

}

console.log(c)