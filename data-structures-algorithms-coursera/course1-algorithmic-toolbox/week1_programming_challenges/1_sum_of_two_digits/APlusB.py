# Input format: Integers a and b on the same line (separated by a space).
# Output format: The sum of a and b.

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

def to_int(a):
    return int(a)

if __name__ == '__main__':
    a, b = map(to_int, input().split())
    print(sum_of_two_digits(a, b))
