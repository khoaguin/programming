// Input: The two integers a, b are given in the same line separated by space.
// Output: The greatest common divisor of a and b

use std::io;
use std::cmp;


fn gcd_naive(a: &u64, b: &u64) -> u64 {
    let mut current_gcd = 1;
    for i in 2..(cmp::min(a, b) + 1) {
        if a % i == 0 && b % i == 0{
            if i > current_gcd {
                current_gcd = i;
            }
        } 
    }
    current_gcd
}


fn gcd_euclid(a: &u64, b: &u64) -> u64 {
    if *b == 0 {
        return *a;
    }
    let a_prime = a % b;

    gcd_euclid(&b, &a_prime)
}


fn main() -> io::Result<()> {
    // get user inputs
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let mut words = buffer.split_whitespace();
    let a: u64 = words.next().unwrap().parse().unwrap();
    let b: u64 = words.next().unwrap().parse().unwrap();

    // println!("{:?}", gcd_naive(&a, &b));
    println!("{:?}", gcd_euclid(&a, &b));

    Ok(())
}