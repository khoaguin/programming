
// Promises and Asynchronous Programming
// async programming, is a method of programming which enables different 
// parts of code to run at changing times, instead of immediately.
// A Promise is a native JavaScript object which has two traits: 
// 1. It receives a single argument which is a function. 
//      This function needs to have two arguments, a `resolve` function and a 
//      `reject` function. The code written inside the promise needs to use one 
//      of these two functions. 
// 2. It can be waited on using the `then` method (and other similar methods), 
//      or the `await` statement
console.log("--- Promises ---");
function sumAsync(x, y) {
    console.log("1. sumAsync is executed");
    const p = new Promise((resolve, reject) => {
        // run this in 500ms from now
        setTimeout(() => {
            console.log("4. Resolving sumAsync's Promise with the result after 500ms");
            resolve(x + y);
        }, 500);

        // we don't need to return anything
        console.log("2. sumAsync Promise is initialized");            
    });
    console.log("3. sumAsync has returned the Promise");
    return p;
}

// let's use the function now
sumAsync(5, 7).then((result) => {
    console.log("[Promises] 5. The result of the addition is:", result);
});


console.log("--- Rejecting promises ---");
function rejectAsync(x, y) {
    return new Promise((resolve, reject) => {
        // run this in 500ms from now
        setTimeout(() => {
            if (x < 0 || y < 0) {
                reject("Negative values received");
            } else {
                resolve(x + y);
            }
        }, 500);

        // we don't need to return anything
    });
}

rejectAsync(-5, 7).then((result) => {
    console.log("The result of the addition is:", result);
}).catch((error) => {
    console.log("[Rejecting promises] Error received:", error);
});

// Async and Await
// The `async` and `await` keywords in JavaScript are used to make asynchronous 
// programming easy, by introducing something called coroutines. 
// A coroutine is a function which can pause its execution and 
// return control to the main loop until some event occurs. 
// It is an alternative approach for using callback functions, which makes 
// it easier to write, understand and maintain.

// The await keyword is a special command which tells JavaScript to stop 
// the execution of the current function until a Promise resolves, 
// and then return the promise's value.
// The await keyword only works inside async functions 
// (which are coroutines, as explained before).

// Instead of writing this ugly code
// function sleep(ms) {
//     return new Promise((resolve) => setTimeout(resolve, ms));
// }
// function sumAsync(x, y) {
//     return new Promise((resolve, reject) => {
//         sleep(500).then(() => {
//             resolve(x + y);
//         });
//     });
// }
// sumAsync(5, 7).then((result) => {
//     console.log("The result of the addition is:", result);
// });

// we can write this beautiful code with async and await
console.log("--- async functions ---");
async function sleep(ms) {
    await new Promise(resolve => setTimeout(resolve, ms));
}
// function sleep(ms) {
//     return new Promise((resolve) => setTimeout(resolve, ms));
// }

async function sumAsync(x, y) {
    // this code waits here for 500 milliseconds
    await sleep(500);
    // done waiting. let's calculate and return the value
    return x+y;
}

// sumAsync is an async function, which means it returns a Promise.
sumAsync(5, 7).then((result) => {
    console.log("[async] The result of the addition is:", result);
});


console.log("--- Finish async experiments! ---");
