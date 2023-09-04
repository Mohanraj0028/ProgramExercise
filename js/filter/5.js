const arrayOfPairs = [
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 30 },
    { name: 'Charlie', age: 22 },
    { name: 'David', age: 28 },
    { name: 'Eve', age: 35 },
    { name: 'Frank', age: 27 },
    { name: 'Grace', age: 31 },
    { name: 'Hannah', age: 29 },
    { name: 'Isaac', age: 26 },
    { name: 'Jane', age: 33 }
];


let b = arrayOfPairs.filter(ages => ages.age > 25)

console.log(b)


