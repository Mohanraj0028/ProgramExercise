let namesArray = [
    { name: 'alice' },
    { name: 'bob' },
    { name: 'carol' },
    { name: 'dave' },
    { name: 'emily' },
    { name: 'frank' },
    { name: 'grace' },
    { name: 'hannah' },
    { name: 'ian' },
    { name: 'jessica' }
  ];
  
b = namesArray.map(e => captalize)

function captalize(e){
    return e.name
}

console.log(b)
  