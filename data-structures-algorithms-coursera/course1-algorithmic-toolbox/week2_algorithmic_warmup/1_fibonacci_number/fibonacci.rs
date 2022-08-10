// Input: An integer n >= 0
// Output: The Fibonnaci number at position n

use std::io;
use std::error::Error;

// recursive solution, slow
fn fibonacci_naive(n: &u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        n => fibonacci_naive(&(n-1)) + fibonacci_naive(&(n-2)),
    }
}

// non-recursive solution, faster
fn fibonacci_fast(n: &u32) -> u64 {
    // your code here
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
    sum
}


fn test_solution() {
    let mut i = 0;
    loop {
        if i == 20 {
            break;
        }
        assert_eq!(fibonacci_naive(&i), fibonacci_fast(&i), 
            "\nF_{:?} = {:?}, your answer = {:?}", i, fibonacci_naive(&i), fibonacci_fast(&i));
        i += 1;
    }
}


fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let n = buffer.trim().parse().unwrap();
    
    test_solution();
    // println!("{}", fibonacci_naive(&n));
    println!("{}", fibonacci_fast(&n));

    Ok(())
}