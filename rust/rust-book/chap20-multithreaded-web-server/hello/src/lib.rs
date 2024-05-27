use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,  // hold on to the receiver
    sender: mpsc::Sender<Job>,  // create a channel and hold on to the sender
}

struct Job;  // hold the closures we want to send down the channel

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            // create some threads and store them in the vector
            workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers , sender}
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static, // we need Send to transfer the closure from
                                      // one thread to another and 'static because
                                      // we don’t know how long the thread will take to execute.
    {
        // send the job it wants to execute through the sender
    }
}

pub struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
    fn new(id: usize) -> Worker {
        let thread = thread::spawn(|| {
            receiver;
        });

        Worker {id, thread}
    }
}