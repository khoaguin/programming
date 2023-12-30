#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        height: 50,
        width: dbg!(30 * scale), // Note that dbg! macro takes ownership of an expression
                                 // Also, dbg! returns ownership of the expression’s value
                                 // so width will have the value of 60
    };

    dbg!(&rect1);

    println!("The area is {}", area(&rect1))
}

fn area(rec: &Rectangle) -> u32 {
    rec.width * rec.height
}
