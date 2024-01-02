use crate::garden::vegetables::Asparagus;

pub mod garden;

fn main() {
    let plant = Asparagus {};
    plant.which();
    println!("I'm growing {:?}!", plant);
}
