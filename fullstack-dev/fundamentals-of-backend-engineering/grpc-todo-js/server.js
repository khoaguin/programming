const grpc = require('grpc');

// we need proto-loader to compile the proton into a bunch of JavaScript files that will actually 
// have your schema and the getters and setters for your schema.
const protoLoader = require('@grpc/proto-loader');

// Load the proto file and the todoPackage
const packageDef = protoLoader.loadSync("todo.proto", {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const todoPackage = grpcObject.todoPackage;

const server = new grpc.Server();
// unsecure server for now - meaning no SSL and plaintext communication between services
server.bind("0.0.0.0:40000", grpc.ServerCredentials.createInsecure());
server.addService(todoPackage.Todo.service, {
    "createTodo": createTodo,
    "readTodos": readTodos,
    "readTodosStream": readTodosStream
});
server.start();

const todos = [];
// gRPC methods always have two parameters: `call` and `callback`
// `call` is the object that represents the call to the server
// `callback` is the function that you call to send data back to the client
function createTodo(call, callback) {
    const todoItem = {
        "id": todos.length + 1,
        "text": call.request.text
    }
    todos.push(todoItem);
    callback(null, todoItem);  // send the todoItem as a response back to the client
}

function readTodosStream(call, callback) {
    todos.forEach(todo => {
        call.write(todo);
    });
    call.end();
}

function readTodos(call, callback) {
    callback(null, {"items": todos});
}
