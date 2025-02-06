/**
 * @typedef {Object} Item
 * @property {string} name - The name of the item
 * @property {?string} [description=null] - Optional description of the item
 * @property {number} price - The price of the item
 * @property {?number} [tax=null] - Optional tax amount
 */


/** @type {Item} */
const myItem = {
    name: "Book",
    description: "A great book",
    price: 29.99,
    tax: 2.50
};


fetch("http://127.0.0.1:8000/items/1", {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(myItem)
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));