#
# Library
#


def fib_recursive(n):
    # base case
    if n == 0 or n == 1:
        return 1

    # kit cat phase, break down
    part1 = fib_recursive(n - 1)
    part2 = fib_recursive(n - 2)

    # reassembly phase
    res = part1 + part2

    return res


#
# Script
#

def main():
    n = 4
    print(fib_recursive(n))


if __name__ == '__main__':
    main()
