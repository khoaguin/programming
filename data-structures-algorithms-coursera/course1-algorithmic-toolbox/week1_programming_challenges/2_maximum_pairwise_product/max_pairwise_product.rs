// Input: A sequence of non-negative integers.
// Output: The maximum value that can be obtained by multiplying 
// two different elements from the sequence.

use std::io;

// Get a sequence of integers from user and return a vector of those integers
fn get_user_input() -> Result<Vec<i64>, io::Error> {
    let mut n_buffer = String::new();
    io::stdin().read_line(&mut n_buffer)?;
    let n: usize = n_buffer.trim().parse().unwrap();
    // println!("{:?}", n);

    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let words = buffer.split_whitespace();
    let vec_str: Vec<&str> = words.collect();
    let vec_int: Vec<i64> = vec_str.iter().map(|&x| x.parse::<i64>().unwrap()).collect();
    assert_eq!(n, vec_int.len(), "You want {} numbers, but entered {} numbers", n, vec_int.len());
    Ok(vec_int)
}

// Finding 2 maximal numbers in a sequence by finding 2 maximal numbers and multiply them
fn maximum_pairwise_product(numbers: &Vec<i64>) -> i64 {
    // Find the index of the first maximum number
    let max_index1 = numbers
                        .iter()
                        .enumerate()
                        .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
                        .map(|(index, _)| index)
                        .unwrap();
    // println!("{:?}", max_index1);

    // Find the index of the second maximum number
    let mut numbers2: Vec<i64> = numbers.clone();
    numbers2.remove(max_index1);
    let max_index2 = numbers2
                        .iter()
                        .enumerate()
                        .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
                        .map(|(index, _)| index)
                        .unwrap();
    let max1 = numbers[max_index1];
    let max2 = numbers2[max_index2];
    // println!("{}, {}", max1, max2);
    
    // 9.00 * 1000.00
    max1 * max2
}

fn main() -> io::Result<()> {
    let numbers: Vec<i64> = get_user_input()?;
    println!("{:?}", maximum_pairwise_product(&numbers));

    Ok(())
}