#
# Library
#


def flatten_list(lst):
    """
    2-part problem
    output == list of elements [5, 6, 8, 10]
    first step: list flattening operation. take everything from nested lists and put it in a list
    second step: remove duplicate items in the list and sort it.

    """

    # base Case
    if len(lst) == 1 and not isinstance(lst[0], list):
        elt = lst[0]
        str_ = [elt]
        return str_

    elif len(lst) == 1 and len(lst[0]) == 1:
        elt = lst[0]
        str_ = elt
        return str_

    elif len(lst) == 1:
        # kit kat part
        sub_list = lst[0]

        part_1 = flatten_list(sub_list[:1])
        part_2 = flatten_list(sub_list[1:])

        # bring together
        res = part_1 + part_2
        return res

    # kit kat part
    part_1 = flatten_list(lst[:1])
    part_2 = flatten_list(lst[1:])

    # bring together
    res = part_1 + part_2
    return res


#
# Script
#

def main():
    a = [5, 10]
    b = [8, a]  # [8, [5, 10]]
    c = [a, b, 6]
    set_ = set(flatten_list(c))
    sorted_ = sorted(set_)
    print(sorted_)


if __name__ == '__main__':
    main()
