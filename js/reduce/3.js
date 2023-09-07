price = [123,321,345,432,456,322]

totalsum = price.reduce((totalprice,e)=>{
    return totalprice+e
},0)


console.log("Average: ",totalsum/price.length)