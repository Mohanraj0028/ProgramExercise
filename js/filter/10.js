let arrayOfStrings = [
    'racecar',
    'hello',
    'level',
    'world',
    'deified',
];

b = arrayOfStrings.filter(str => str == str.split('').reverse().join(''))

console.log(b)