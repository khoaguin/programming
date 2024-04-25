use std::env;
use std::process;

use minigrep::Config;

fn main() {
    // env::args() returns std::env::Args which implements the `Iterator` trait and returns `String` values
    let config = Config::build(env::args()).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}"); // print errors to stderr stream
        process::exit(1);
    });

    println!(
        "Searching for '{}' in file '{}'",
        config.query, config.file_path
    );

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}"); // print errors to stderr stream
        process::exit(1);
    }
}
