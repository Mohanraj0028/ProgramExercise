let students = [
    { name: "Alice" },
    { name: "Bob" },
    { name: "Carol" },
    { name: "David" }
  ];
  
  let a = 1;
  students = students.map(e => {
    e['sal'] = a * 100;
    return e;
  });
  
  console.log(students);
  