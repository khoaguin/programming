/**
 * @typedef {Object} Item
 * @property {string} name - The name of the item
 * @property {?string} [description=null] - Optional description of the item
 * @property {number} price - The price of the item
 * @property {?number} [tax=null] - Optional tax amount
 * @property {string} body - JSON stringified body
 */

/**
 * @typedef {"RPC_NOT_FOUND" | "RPC_PENDING" | "RPC_COMPLETED" | "RPC_ERROR"} RPCStatusCode
 */


/** @type {Item} */
const myItem = {
    name: "Book",
    description: "A great book",
    price: 29.99,
    tax: 2.50,
};

/**
 * @typedef {Object} ItemResponse
 * @property {string} id - The response ID
 * @property {RPCStatusCode} status - The RPC status code
 * @property {Item|Array<Item>} items - Single item or array of items
 */


// promise chaining syntax
// fetch("http://127.0.0.1:8000/items/1", {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(myItem)
// })
// .then(response => response.json())
// .then(data => console.log('Success:', data))
// .catch(error => console.error('Error:', error));


// try await syntax
try {
    const response = await fetch("http://127.0.0.1:8000/items/2", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(myItem)
    });
    const data = await response.json();
    /** @type {ItemResponse} */

    for (let item of data.items) {
        // item.body = atob(item.body);
        console.log('item = ', item);
        console.log('item.body = ', atob(item.body));
    }

    const itemResponse = {
        id: data.id,
        status: data.status,
        items: data.items
    }

    
    console.log('Success. itemResponse = ', itemResponse);
} catch (error) {
    console.error('Error:', error);
}