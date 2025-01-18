const newVariable = null;
console.log(newVariable); //prints undefined

var myArray = []
myArray[1] = "hello"
console.log(myArray);

var myArray = ["string", 10, {}]
console.log(myArray);

var myStack = [];
myStack.push(1);
myStack.push(2);
myStack.push(3);
console.log(myStack);

console.log(myStack.pop());
console.log(myStack);

var myQueue = [];
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);

console.log(myQueue.shift());
console.log(myQueue.shift());
console.log(myQueue.shift());

console.log(myQueue);

var myArray = [1,2,3];
myArray.unshift(0);
console.log(myArray);       // will print out 0,1,2,3


var myArray = [0,1,2,3,4,5,6,7,8,9];
var splice = myArray.splice(3,5);  // Start at index 3 (where the value is 3)
                                // Remove 5 elements (3,4,5,6,7)

console.log(splice);        // will print out 3,4,5,6,7
console.log(myArray);       // will print out 0,1,2,8,9

var name = "John";
console.log("Hello " + name + "!");
console.log("The meaning of life is " + 42);
console.log(42 + " is the meaning of life");

console.log(1 + "1");   // outputs "11" default primitive value is a string

if (1)
    {
        console.log("Hello John, how are you?");
    } else {
        console.log("Then what is your name?");
}


console.log("1" == 1); // true
console.log("1" === 1); // strict comparison - output false

var foo = 1;
var bar = 2;
var moo = 3;

if (foo < bar && moo > bar)
{
    console.log("foo is smaller than bar AND moo is larger than bar.");
}

if (foo < bar || moo > bar)
{
    console.log("foo is smaller than bar OR moo is larger than bar.");
}


// JavaScript is a functional language, and for object oriented programming 
// it uses both objects and functions, but objects are usually used as a data s
// tructure, similar to a dictionary in Python or a map in Java

// object
var personObject = {
    firstName : "John",
    lastName : "Smith"
}
personObject.age = 23;
personObject["salary"] = 14000;

for (var member in personObject)
    {
        if (personObject.hasOwnProperty(member))
        {
            console.log("the member " + member + " of personObject is " + personObject[member])
        }
    }
    
function greet(name)
{
    return "Hello " + name + "!";
}

console.log(greet("Eric"));      // prints out Hello Eric!


var greet = function(name)
{
    return "Hello " + name + "!";
}

console.log(greet("Eric"));      // prints out Hello Eric!


// confirm("Hi!");
// prompt("Bye!");
// alert("Hello");


// Callbacks in JavaScript are functions that are passed as arguments to other functions
var callback = function() {
    console.log("Done!");
}

setTimeout(callback, 2000);  // waits 2 seconds before calling the `callback` function


// Arrow Functions
const greetArrowFunc = (name) => { return "Hello " + name + "!"; }
console.log(greetArrowFunc("Eric"));      // prints out Hello Eric!

let numbers = [3, 5, 8, 9, 2];

// Old way
function multiplyByTwo(number){
    return number * 2;
}
let multipliedNumbers = numbers.map(multiplyByTwo);
console.log(multipliedNumbers);              // prints out: 6, 10, 16, 18, 4

// Using ES6 arrow functions
const multiplyByTwo2 = number => number * 2;
let multipliedNumbers2 = numbers.map(multiplyByTwo);
console.log(multipliedNumbers2);              // prints out: 6, 10, 16, 18, 4
