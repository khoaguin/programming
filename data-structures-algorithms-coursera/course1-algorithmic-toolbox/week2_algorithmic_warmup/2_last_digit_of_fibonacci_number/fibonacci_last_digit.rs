// Task: Given an integer n, find the last digit of the 
//        n-th Fibonacci number (that is, Fn mod 10)
// Input: A single integer n
// Output: The last digit of Fn
// Example Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

use std::io;
use std::error::Error;


fn last_digit_fibonacci_naive(n: &u32) -> u64 {
    if *n == 1 {
        return 1;
    }
    let mut sum = 0;
    let mut last = 0;
    let mut curr = 1;
    for _i in 1..*n {
        sum = last + curr;
        last = curr;
        curr = sum;
    }
    sum % 10
}


fn last_digit_fibonacci_fast(n: &u32) -> u64 {
    if *n == 1{
        return 1;
    }
    let mut sum = 0;
    let mut previous = 0;
    let mut current = 1;
    for _ in 1..*n {
        sum = (previous + current) % 10;
        previous = (current) % 10;
        current = sum;
    }
    sum
}

// only test the first 30 sequences
fn test_solution() {
    let mut i = 0;
    loop {
        if i == 30 {
            break;
        }
        assert_eq!(last_digit_fibonacci_naive(&i), last_digit_fibonacci_fast(&i), 
            "\nCorrect = {:?}, your answer = {:?}", 
                last_digit_fibonacci_naive(&i), last_digit_fibonacci_fast(&i));
        i += 1;
    }
    println!("Test passed!");
}


fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let n = buffer.trim().parse().unwrap();
    
    // test_solution();
    // println!("{}", last_digit_fibonacci_naive(&n));
    println!("{}", last_digit_fibonacci_fast(&n));

    Ok(())
}