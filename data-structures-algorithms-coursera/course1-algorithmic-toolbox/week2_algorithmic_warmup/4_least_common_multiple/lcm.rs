// Input: The two integers a and a are given in the same line separated by space
// Output: The least common multiple of a and b

use std::io;


fn lcm_naive(a: &u64, b: &u64) -> u64 {
    let d = a * b;
    for l in 1..(d+1) {
        if l % a == 0 && l % b == 0 {
            return l;
        } 
    }

    0
}


fn gcd(a: &u64, b: &u64) -> u64 {
    if *b == 0 {
        return *a;
    }
    let c = a % b;
    gcd(&b, &c)
}   


fn lcm_fast(a: &u64, b: &u64) -> u64 {
    let m = gcd(a, b);
    let c = a / m;
    c * b
}


fn main() -> io::Result<()> {
    // get user inputs
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let mut words = buffer.split_whitespace();
    let a: u64 = words.next().unwrap().parse().unwrap();
    let b: u64 = words.next().unwrap().parse().unwrap();

    // println!("{:?}", lcm_naive(&a, &b));
    println!("{:?}", lcm_fast(&a, &b));

    Ok(())
}