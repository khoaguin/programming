pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
        // assert_eq!(2 + 2, 5);
    }

    #[test]
    #[should_panic(expected = "less than or equal to 100")]
    fn greater_than_100() {
        assert!(200 < 100);
    }
}
