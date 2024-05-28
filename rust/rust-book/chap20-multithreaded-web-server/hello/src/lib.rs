use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};

pub struct ThreadPool {
    workers: Vec<Worker>,      // hold on to the receiver
    sender: mpsc::Sender<Job>, // create a channel and hold on to the sender
}

struct Job; // hold the closures we want to send down the channel

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        // The `Arc` type will let multiple workers own the receiver
        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            // create some threads and store them in the vector
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool { workers, sender }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static, // we need Send to transfer the closure from
                                      // one thread to another and 'static because
                                      // we don’t know how long the thread will take to execute.
    {
        let job = Box::new(f);

        // send the job it wants to execute through the sender
        self.sender.send(job).unwrap();
    }
}

pub struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // we need the closure to loop forever, asking the receiving end of
        // the channel for a job and running the job when it gets one.
        let thread = thread::spawn(move || loop {
            let job = receiver
                .lock() //  we first call lock on the receiver to acquire the mutex
                .unwrap() // then we call unwrap to panic on any errors
                .recv() // If we get the lock on the mutex, we call recv to receive a Job from the channel
                .unwrap();
            println!("Worker {id} got a job; executing.");
            job();
        });

        Worker { id, thread }
    }
}
