#!/bin/bash

cargo --version
rm -rf hello_cargo
cargo new hello_cargo
echo "--- hello_cargo project created, let's see what's inside: "
ls hello_cargo
echo "--- building hello_cargo ---"
cd hello_cargo
cargo build
echo "--- running hello_cargo ---"
./target/debug/hello_cargo
echo "--- checking if the program is compilable ---"
cargo check