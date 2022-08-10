# Input: The two integers a and a are given in the same line separated by space
# Output: The least common multiple of a and b


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return gcd(b, c);


def lcm_fast(a, b):
    m = gcd(a, b)
    c = a // m
    return b * c


if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))

