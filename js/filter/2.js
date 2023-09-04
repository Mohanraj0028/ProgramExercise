const products = [
    { name: 'Product 1', price: 20 },
    { name: 'Product 2', price: 30 },
    { name: 'Product 3', price: 15 },
    { name: 'Product 4', price: 25 },
    { name: 'Product 5', price: 10 },
    { name: 'Product 6', price: 40 },
    { name: 'Product 7', price: 12 },
    { name: 'Product 8', price: 35 },
    { name: 'Product 9', price: 18 },
    { name: 'Product 10', price: 22 }
];

let maxvalue = 15
let b = products.filter(products => products.price <= maxvalue)

// function maxprice(products){
//     if(products.price > 15){
//         return products
//     }
// }

console.log(b);
