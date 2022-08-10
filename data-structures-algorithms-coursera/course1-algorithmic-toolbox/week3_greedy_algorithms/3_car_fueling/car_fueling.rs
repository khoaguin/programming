// Input: The first line contains an integer d (the distance between 2 cities). 
//        The second line contains an integer m (the maximum miles a car can travel on a full tank). 
//        The third line specifies an integer n (the number of gas stops between 2 cities). 
//        Finally, the last line contains integers stop_1, stop_2, ..., stop_n (distances along the way).
// Output: The minimum number of refills needed. 
//         We assume that the car starts with a full tank. 
//         If it is not possible to reach the destination, output −1

use std::io;
use std::error::Error;


fn get_user_integer() -> u32 {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed to read line");
    
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


fn compute_min_refills(distance: u32, tank: u32, num_stops: usize, stops: &Vec<u32>) -> i32 {
    let mut limit: u32 = tank;
    let mut current_stop: usize = 0;
    let mut num_refills: i32 = 0;
    // let n: usize = stops.len();

    while limit < distance {
        // cases when we cannot reach the destination
        if current_stop >= num_stops || limit < stops[current_stop] {
            return -1;
        }
        // find the furthest reachable stop
        while current_stop < num_stops - 1 && stops[current_stop + 1] <= limit {
            current_stop += 1;
        }
        limit = stops[current_stop] + tank;
        current_stop += 1;
        num_refills += 1;
    }
    
    num_refills
}


fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let distance: u32 = get_user_integer();
    let tank: u32 = get_user_integer();
    let num_stops: usize = get_user_integer() as usize;
    let stops: Vec<u32> = get_user_vector();

    println!("{}", compute_min_refills(distance, tank, num_stops, &stops));

    Ok(())
}