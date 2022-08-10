// Input: An integer n >= 0
// Output: The Fibonnaci number at position n

use std::io;
use std::error::Error;

fn fibonacci_naive(n: &i32) -> i64 {
    match n {
        0 => 0,
        1 => 1,
        n => fibonacci_naive(&(n-1)) + fibonacci_naive(&(n-2)),
    }
}

fn fibonacci_fast(n: &i32) -> i64 {
    // your code here
    0
}

fn test_solution() {
    let mut i = 0;
    loop {
        if i == 20 {
            break;
        }
        assert_eq!(fibonacci_naive(&i), fibonacci_fast(&i), 
            "\nF_{:?} = {:?}, your answer = {:?}", &i, fibonacci_naive(&i), fibonacci_fast(&i));
        i += 1;
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let n = buffer.trim().parse().unwrap();
    
    test_solution();
    println!("{}", fibonacci_naive(&n));

    Ok(())
}