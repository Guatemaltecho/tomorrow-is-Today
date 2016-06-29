#
# Library
#


def int_to_string(lst):
    """
    create a fn called int_to_string, takes in a lst of integers and converts them all to strings. Use Recursion
    input = [0,1,2,3,4] ---- output == [str(0), str(1)...str(4)]
    """

    if len(lst) == 1:
        elt = lst[0]
        str_ = [str(elt)]
        return str_

    part_1 = int_to_string(lst[:1])
    part_2 = int_to_string(lst[1:])

    res = part_1 + part_2
    return res


#
# Script
#

def main():
    lst = range(5)
    print(int_to_string(lst))


if __name__ == '__main__':
    main()
