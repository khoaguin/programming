# Minigrep

In this project, we will make our own version of the classic command line search tool `grep` (_globally search a regular expression and print_)

## What the program does?

Searches a specified file for a specified string:

1. `grep` takes as its arguments a file path and a string
2. Reads the file, finds lines in that file that contain the string argument, and prints those lines

## What we will learn?

- Organizing code (using what you learned about `modules` in Chapter 7)
- Using vectors and strings (collections, Chapter 8)
- Handling errors with `stderr` (Chapter 9)
- Using traits and lifetimes where appropriate (Chapter 10)
- Writing tests (Chapter 11)
- Briefly introduce closures, iterators, and trait objects (Chapters 13 and 17)

## Running

```bash
cargo run -- searchstring poem.txt
```

or

```bash
IGNORE_CASE=1 cargo run -- searchstring poem.txt
```
