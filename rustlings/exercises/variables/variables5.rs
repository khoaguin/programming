// variables5.rs
//
// Execute `rustlings hint variables5` or use the `hint` watch subcommand for a
// hint.

fn main() {
    // As you saw in the guessing game tutorial in Chapter 2, you can declare a new
    // variable with the same name as a previous variable. Rustaceans say that the
    // first variable is shadowed by the second, which means that the second variable
    // is what the compiler will see when you use the name of the variable.
    let number = "T-H-R-E-E"; // don't change this line
    println!("Spell a Number : {}", number);
    let number: i32 = 3; // don't rename this variable
    println!("Number plus two is : {}", number + 2);
}
