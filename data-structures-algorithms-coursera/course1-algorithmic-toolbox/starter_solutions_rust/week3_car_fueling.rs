// Input: The first line contains an integer d (the distance between 2 cities). 
//        The second line contains an integer m (the maximum miles a car can travel on a full tank). 
//        The third line specifies an integer n (the number of gas stops between 2 cities). 
//        Finally, the last line contains integers stop_1, stop_2, ..., stop_n (distances along the way).
// Output: The minimum number of refills needed. 
//         We assume that the car starts with a full tank. 
//         If it is not possible to reach the destination, output −1

use std::io;
use std::error::Error;


fn get_user_integer() -> i32 {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer);
    
    buffer.trim().parse().expect("Not an integer!")
}


fn get_user_vector() -> Vec<u32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Failed to read line");
    let inputs: Vec<u32> = line.split_whitespace()
                               .map(|x| x.parse().expect("Not an integer!"))
                               .collect();
    inputs
}


fn compute_min_refills(distance: i32, tank: i32, stops: &Vec<u32>) -> i32 {
    // Your code here
    0
}


fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let distance = get_user_integer();
    let tank = get_user_integer();
    let num_stops = get_user_integer();
    let stops = get_user_vector();

    println!("stops: {:?}", stops);
    println!("{}", compute_min_refills(distance, tank, &stops));

    Ok(())
}