const arrayOfPairs = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 35 },
    { name: "David", age: 28 },
    { name: "Eve", age: 22 },
    { name: "Frank", age: 40 },
    { name: "Grace", age: 32 },
    { name: "Hank", age: 29 },
    { name: "Ivy", age: 27 },
    { name: "Jack", age: 31 }
  ];

  average = arrayOfPairs.reduce((sum,e)=>{
    return sum = sum + e.age
  },0)

  console.log("Average: ",average/arrayOfPairs.length)