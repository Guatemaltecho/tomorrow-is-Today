###########
# Imports #
###########

from list_adders_lib import list_add_one, add_n_to_list

###########
# Library #
###########

def make_list():
    x = range(10)
    return x

def uselistfunc(fn, lst):
    return fn(lst)

def is_even(n):
    return n % 2 == 0

def get_evens_map(lst):
    return map(is_even, lst)

def get_evens_filter(lst):
    return filter(is_even, lst)

##########
# Script #
##########

def main():
    fn = lambda lst: add_n_to_list(2, lst)
    lst = make_list()
    lst2 = uselistfunc(fn, lst)
    lst3 = uselistfunc(fn, lst2)
    print lst
    print lst2
    print get_evens_filter(lst3)
    print get_evens_map(lst3)


if __name__ == '__main__':
    main()
