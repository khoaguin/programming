// Task: The goal in this problem is to find the minimum number of 
//  coins needed to change the input value (an integer) into coins 
//  with denominations 1, 5, and 10.
// Input Format: The input consists of a single integer m (1 <= m <= 10^3).
// Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes m


use std::io;
use std::error::Error;


fn change(m: &u32) -> u32 {
    // your code here
    0
}

fn main() -> Result<(), Box<dyn Error>> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let m = buffer.trim().parse().unwrap();

    println!("{}", change(&m));

    Ok(())
}