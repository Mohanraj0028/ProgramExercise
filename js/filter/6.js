const arrayOfObjects = [
    { name: 'Alice', hobbies: ['Reading', 'Painting', 'Hiking'] },
    { name: 'Bob', hobbies: ['Gaming', 'Cooking', 'Photography'] },
    { name: 'Charlie', hobbies: ['Traveling', 'Swimming', 'Music'] },
    { name: 'David', hobbies: ['Cycling', 'Yoga', 'Cooking'] },
    { name: 'Eve', hobbies: ['Dancing', 'Gardening', 'Running'] },
    { name: 'Frank', hobbies: ['Writing', 'Drawing', 'Basketball'] },
    { name: 'Grace', hobbies: ['Painting', 'Singing', 'Hiking'] },
    { name: 'Hannah', hobbies: ['Photography', 'Gaming', 'Cooking'] },
    { name: 'Isaac', hobbies: ['Swimming', 'Reading', 'Traveling'] },
    { name: 'Jane', hobbies: ['Yoga', 'Cycling', 'Running'] }
];

let ourhobby = "Cooking"

b = arrayOfObjects.filter(e => e.hobbies.includes(ourhobby))

console.log(b)
