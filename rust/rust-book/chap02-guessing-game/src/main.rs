use std::io; // bring the std's io input/output into
             // scope since it's not in prelude
use rand::Rng; // to create random numbers
use std::cmp::Ordering; // The Ordering type is another
                        // enum and has the variants Less,
                        // Greater, and Equal.

fn main() {
    println!("--- Guess the number! ---");

    // `rand::thread_rng()`` gives us a random number generator
    // `gen_range()` is defined by the `Rng` trait
    // `start..=end` is a range expression that's inclusive on both ends
    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("Please input your guess.");

    loop {
        let mut guess = String::new(); // growable size at runtime

        io::stdin()
            .read_line(&mut guess) // will return a `Result` enum that encodes error-handling information
            .expect("Failed to read line"); // `expect` is a `Result`'s method
                                            // If this instance of `Result` is an `Err` value,
                                            // `expect` will cause the program to crash and
                                            // display the message that you passed as an
                                            // argument to `expect`. If the instance is `Ok`,
                                            // `expect` returns the value hold by `Ok`

        // `String.trim()`` eliminates any whitespace at the beginning and end
        // `String.parse()` converts a string to another type
        let guess_int: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(e) => {
                println!("Error: {}. Please enter a number!", e);
                continue; // go to the next iteration of the loop and ask for another guess
            }
        };
        println!("You guessed: {guess_int}");
        println!("The secret number is: {}", secret_number);

        match guess_int.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
