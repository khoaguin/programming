use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    // connecting to a port to listen to ("binding" to a port).
    // try to bind to port 80, you will get Err: PermissionDenied.
    // bind will also fail if we run two instances of our program that listen to the same port.
    let listener: TcpListener = TcpListener::bind("127.0.0.1:7878").unwrap();
    println!("TCP listener: {:?}", listener);

    // The `incoming()` method on `TcpListener` returns an iterator that
    // gives us a sequence of streams (of type `TcpStream`).
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        println!("Connection established with stream: {:?}", stream);
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    // BufReader adds buffering by managing calls to the `std::io::Read` trait methods for us.
    let buf_reader = BufReader::new(&mut stream);

    // get one request from the stream, we take lines until we get a line that is the empty string
    // let http_request: Vec<_> = buf_reader
    //     .lines()
    //     .map(|res| res.unwrap())
    //     .take_while(|line| !line.is_empty())
    //     .collect();
    // println!("Request: {:#?}", http_request);

    // validating the request that if it looks for the `/` (root) path
    let request_line = buf_reader.lines().next().unwrap().unwrap();  //  the first line of request
    
    let (status_line, filename) = if request_line == "GET / HTTP/1.1" {
        ("HTTP/1.1 200 OK", "templates/hello.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND", "templates/404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response =
        format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");

    stream.write_all(response.as_bytes()).unwrap();

}
