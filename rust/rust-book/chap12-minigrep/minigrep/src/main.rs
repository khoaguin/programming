use std::env;
use std::process;

use minigrep::Config;

fn main() {
    let args: Vec<String> = env::args().collect(); // collect arguments

    let config = Config::build(&args).unwrap_or_else(|err| {
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
