// Input format: Integers a and b on the same line (separated by a space).
// Output format: The sum of a and b.

use std::io;

fn main() -> io::Result<()> {
    // println!("Please enter 2 integers separated by a space");
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let mut words = buffer.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    println!("{}", a+b);
    
    Ok(())
}