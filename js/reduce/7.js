const arrayOfStrings = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon"
  ];


  str = arrayOfStrings.reduce((acc,e)=>{
    acc.push({
        "name":e,
        "legnt":e.length
    });
    return acc
  },[])

  console.log(str)


  