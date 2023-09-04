const arrayOfObjects = [
    { name: 'Alice', grade: 85 },
    { name: 'Bob', grade: 92.5 },
    { name: 'Charlie', grade: 78.5 },
    { name: 'David', grade: 91 },
    { name: 'Eve', grade: 88.5 },
    { name: 'Frank', grade: 75 },
    { name: 'Grace', grade: 96 },
    { name: 'Hannah', grade: 89.5 },
    { name: 'Isaac', grade: 82 },
    { name: 'Jane', grade: 90.5 }
];

b = arrayOfObjects.filter(e => e.grade>85)

console.log(b)