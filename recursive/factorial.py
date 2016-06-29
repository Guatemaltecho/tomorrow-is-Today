#
# Library
#


def factorial_operators(n):
    """
    Factorial operator == 5! ==> (5*4*3*2*1) == 5*4!
    Given n, return that number's factorial using recursion
    input == 5, output == 120
    """
    if n == 0 or n == 1:
        return 1

    part_1 = n  # 5
    part_2 = factorial_operators(n - 1)  # 4!

    res = part_1 * part_2  # 5! * 4!
    return res


#
# Script
#

def main():
    n = 5
    print(factorial_operators(n))


if __name__ == '__main__':
    main()
