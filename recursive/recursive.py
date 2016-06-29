#
# Library
#


def add1_to_list_recursive(lst):
    if len(lst) == 1:
        return [lst[0] + 1]

    first_part = add1_to_list_recursive(lst[:1])
    second_part = add1_to_list_recursive(lst[1:])
    res = first_part + second_part
    return res


#
# Script
#

def main():
    lst = range(5)
    res = add1_to_list_recursive(lst)
    print(res)


if __name__ == '__main__':
    main()