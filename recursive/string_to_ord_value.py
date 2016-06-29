#
# Library
#


def string_to_ord_value_list(s):
    """
    take function that takes in a string and returns a list of ordinal values of the letters
    so if string is abc output should be my_list = [97,98,99]
    use function ord()

    """
    if len(s) == 1:
        ord_value = ord(s[0])
        res = [ord_value]
        return res

    part_1 = string_to_ord_value_list(s[:1])
    part_2 = string_to_ord_value_list(s[1:])

    res = part_1 + part_2
    return res


#
# Script
#

def main():
    s = "abc"
    print(string_to_ord_value_list(s))


if __name__ == '__main__':
    main()
