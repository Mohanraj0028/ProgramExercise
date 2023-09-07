const products = [
    { name: "Product 1", price: 10.99 },
    { name: "Product 2", price: 24.99 },
    { name: "Product 3", price: 7.49 },
    { name: "Product 4", price: 15.99 },
    { name: "Product 5", price: 19.95 },
    { name: "Product 6", price: 5.99 },
    { name: "Product 7", price: 29.99 },
    { name: "Product 8", price: 12.49 },
    { name: "Product 9", price: 8.99 },
    { name: "Product 10", price: 22.99 },
  ];


  totalprice = products.reduce((total,e)=>{
    return total = total+e.price
  },0)

  console.log(totalprice)