let students = [
  { name: "alice", age: 20 },
  { name: "bob", age: 22 },
  { name: "carol", age: 21 },
  { name: "david", age: 19 },
  { name: "eva", age: 23 },
  { name: "frank", age: 18 },
  { name: "grace", age: 20 }
];


function cap(val){

  for(let i=0;i<=students.length;i++){

      return val.name.charAt(0).toUpperCase() + val.name.slice(1)
      

  }

}

let name = students.map(cap)

console.log(name)