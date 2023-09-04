const arrayOfObjects = [
    { name: 'Alice', email: 'alice@example.com' },
    { name: 'Bob', email: 'bob@gmail.com' },
    { name: 'Charlie', email: 'charlie@example.com' },
    { name: 'David', email: 'david@hotmail.com' },
    { name: 'Eve', email: 'eve@gmail.com' },
];

b = arrayOfObjects.filter(e => e.email.includes("example.com"))

console.log(b)