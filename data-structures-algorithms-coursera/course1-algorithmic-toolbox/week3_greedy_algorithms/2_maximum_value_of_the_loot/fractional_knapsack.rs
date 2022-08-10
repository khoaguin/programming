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
use std::cmp;


fn get_user_input() -> Vec<u32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Failed to read line");
    let inputs: Vec<u32> = line.split_whitespace()
            .map(|x| x.parse().expect("Not an integer!"))
            .collect();

    inputs
}


fn most_expensive_index(values: &Vec<u32>, weights: &Vec<u32>) -> usize {
    let mut max_index = 0;
    let mut most_expensive: f64 = -1.0;
    for (i, v) in values.iter().enumerate() {
        let cost: f64 = (*v as f64) / (weights[i] as f64);
        if cost > most_expensive {
            max_index = i;
            most_expensive = cost;
        }
    }
    
    max_index
}


fn get_optimal_value(capacity: &u32, values: &Vec<u32>, weights: &Vec<u32>) -> f64 {
    // Idea: Get the most expensive item first until the bag is full
    // Base case
    if *capacity == 0 || weights.len() == 0 {
        return 0.0;
    }
    // Recursive case
    let m = most_expensive_index(&values, &weights);
    let amount_taken = cmp::min(capacity, &weights[m]);
    let value_taken: f64 = (*amount_taken as f64) * (values[m] as f64 / weights[m] as f64);
    // Remove the taken item from weights and values
    let new_capacity: u32 = capacity - amount_taken;
    let mut new_weights: Vec<u32> = weights.to_vec();
    new_weights.remove(m);
    let mut new_values: Vec<u32> = values.to_vec();
    new_values.remove(m);

    value_taken + get_optimal_value(&new_capacity, &new_values, &new_weights)
}


pub fn main() -> Result<(), Box<dyn Error>> {
    // get the first input line
    let inp = get_user_input();
    let n = inp[0];
    let capacity = inp[1];
    // get the next n lines
    let mut values: Vec<u32> = Vec::new();
    let mut weights: Vec<u32> = Vec::new();
    let mut i = n;
    while i > 0 {
        let inp = get_user_input();
        values.push(inp[0]);
        weights.push(inp[1]);
        i = i - 1;
    }

    println!("{:.10}", get_optimal_value(&capacity, &values, &weights));

    Ok(())
}