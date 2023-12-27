#!/bin/bash

rustc main.rs  # compile main.rs
./main  # Rust is an ahead-of-time compiled language, meaning you can compile a 
        # program and give the executable to someone else, and they can run it 
        # even without having Rust installed.