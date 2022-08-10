// Input: The first line of the input contains the number n of items 
// and the capacity W of a knapsack. The next n lines define the values 
// and weights of the items. The i-th line contains integers v_i and w_i — the
// value and the weight of i-th item, respectively.
// Output: the maximal value of fractions of items that fit into the knapsack. 
// The absolute value of the difference between the answer of your program and 
// the optimal value should be at most 1e−3. To ensure this, output your answer 
// with at least four digits after the decimal point (otherwise your answer, 
// while being computed correctly, can turn out to be wrong because of rounding issues).

use std::io;
use std::error::Error;


fn get_user_input() -> Vec<u32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Failed to read line");
    let inputs: Vec<u32> = line.split_whitespace()
            .map(|x| x.parse().expect("Not an integer!"))
            .collect();

    inputs
}


fn get_optimal_value(capacity: &u32, values: &Vec<u32>, weights: &Vec<u32>) -> f32{
    // your code here
    0.0
}


pub fn main() -> Result<(), Box<dyn Error>> {
    let inp = get_user_input();
    let n = inp[0];
    let capacity = inp[1];

    let mut values: Vec<u32> = Vec::new();
    let mut weights: Vec<u32> = Vec::new();
    let mut i = n;
    while i > 0 {
        let inp = get_user_input();
        values.push(inp[0]);
        weights.push(inp[1]);
        i = i - 1;
    }

    println!("{:.4}", get_optimal_value(&capacity, &values, &weights));

    Ok(())
}