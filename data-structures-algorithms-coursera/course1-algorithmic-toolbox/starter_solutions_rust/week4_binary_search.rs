// Input: The first two lines of the input contain an integer n and a sequence 
//        a0 < a1 < · · · < an − 1 of n distinct positive integers in increasing order. 
//        The next two line contain an integer k and k positive integers b0, b1, . . . , bk − 1.
// Output: For all i from 0 to k − 1, output an index 0 ≤ j ≤ n − 1 of the first occurrence of 
//         bi (i.e., aj = bi) or −1 if there is no such index

use std::io;
use std::error::Error;
// use rand::Rng;  // use if you want to stress test


fn get_user_int() -> u32 {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed to read line");

    buffer.trim().parse().expect("Not an integer")
}

fn get_user_vec(n: u32) -> Vec<u32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Failed to read line");
    let inputs: Vec<u32> = line.split_whitespace()
                               .map(|x| x.parse().expect("Not an integer"))
                               .collect();
    assert!(inputs.len() == (n as usize));

    inputs
}

fn binary_search(a: &Vec<u32>, x: u32) -> i32 {
    // Your code here

    -1
}

fn linear_search(a: &Vec<u32>, x: u32) -> i32 {
    for (i, v) in a.iter().enumerate() {
        // println!("{}: {}", i, v);
        if *v == x {
            return i as i32;
        }
    }
    -1
}

// Comment out if you want to test your solution with linear search
// fn stress_test() {
//     loop {    
//         let mut rng = rand::thread_rng();
//         let n = rng.gen_range(5..20);
//         let mut a: Vec<u32> = vec![0; n];
//         for i in &mut a {
//             *i = rng.gen_range(1..100);
//         }
//         a.sort();
//         let k: u32 = rng.gen_range(1..100);
//         let res1 = linear_search(&a, k);
//         let res2 = binary_search(&a, k);
//         if res1 != res2 {
//             println!("Wrong answer!");
//             for i in &mut a {
//                 print!("{} ", i);
//             }
//             println!("k = {}", k);
//             println!("linear search = {}, binary search = {}", res1, res2);
//             break;
//         } else {
//             println!("Ok!");
//         }
//     }
// }


fn main() -> Result<(), Box<dyn Error>> {
    // get user input
    let n: u32 = get_user_int();
    let a: Vec<u32> = get_user_vec(n);
    let k: u32 = get_user_int();
    let b: Vec<u32> = get_user_vec(k);

    for bi in b {
        // replace linear_search with binary_search
        print!("{} ", binary_search(&a, bi));
    }

    // stress_test();

    Ok(())
}