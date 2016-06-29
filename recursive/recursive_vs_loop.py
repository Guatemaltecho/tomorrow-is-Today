#
# Library
#


def beginning(lst):
    begn = slice(0, 1)
    res = lst[begn]
    return res


def first(lst):
    """return the first element from the list"""
    res = lst[0]
    return res


def last(lst):
    """return the last element from the list"""
    res = lst[-1]
    return res


def rest(lst):
    res = lst[1:]
    return res


# recursive
def my_func(lst):
    if len(lst) == 1:
        return lst

    part_1 = my_func(beginning(lst))
    part_2 = my_func(rest(lst))

    res = part_1 + part_2
    return res


def transfer(accum, seq):
    """transfers elements from seq to accum, 1 element at a time"""
    # base case
    if len(seq) == 0:
        return accum

    nxt = seq[0]
    _accum = accum + [nxt]
    _seq = rest(seq)  #

    res = transfer(_accum, _seq)
    return res


def find_recursion_limit():
    safety_stop = 1200
    i = 0
    try:
        while True:
            transfer(accum=[], seq=range(i))
            i += 1
            if i >= safety_stop:
                return -1
    except RuntimeError:
        return i


def iterate_through_recursions(n):
    i = 0
    while True:
        transfer([], range(i))
        i += 1
        if i >= n:
            break


def count_until(n):
    count = 0
    while True:
        if count >= n:
            break
        count += 1

    return count


def iterative_transfer(accum, seq):
    while True:
        if len(seq) == 0:
            break

        nxt = seq[0]
        accum = accum + [nxt]
        seq = seq[1:]

    return accum


def summate(accum, seq):
    if len(seq) == 0:
        return accum

    nxt = first(seq)
    part_1 = accum + nxt
    part_2 = rest(seq)

    res = summate(part_1, part_2)
    return res


def iterative_summate(accum, seq):
    while True:
        if len(seq) == 0:
            break

        nxt = seq[0]
        accum = accum + nxt
        seq = seq[1:]

    return accum


def summate_list(accum, seq):
    """ accum is a list and seq is a list. both of integers. results should be the progressive summation of the seq.
    so if accum is an empty list and seq is range(5), the result should be [0,1,3,7,11] ~ something like this
    [0,1,2,3,4]
    [0,1,3,6,10] """
    if len(accum) == 0:
        _accum = accum + [first(seq)]
        _seq = rest(seq)
    else:
        # Aliasing
        _accum = accum
        _seq = seq

    if len(seq) == 0:
        return accum

    nxt = _seq[0]
    part_1 = _accum + [last(_accum) + nxt]
    part_2 = rest(_seq)

    res = summate_list(part_1, part_2)
    return res


def iterative_summate_list(accum, seq):
    _accum, _seq = accum, seq
    if len(_accum) > 0:
        res = iterative_summate_list(accum=[], seq=_accum + _seq)
        return res

    if len(_accum) == 0:
        nxt = _seq[0]
        _accum = _accum + [nxt]
        _seq = _seq[1:]

    while True:
        if len(_seq) == 0:
            break

        nxt = _seq[0]
        _accum = _accum + [_accum[-1] + nxt]
        _seq = _seq[1:]

    return _accum


def my_reduce(fn, seq, default):
    """ transfer 1 element at a time to accum in whatever manner is specified by our function
     fn has to meet the following criteria - must take 2 arguments, accum and nxt.

     fn(accum, nxt)
     where nxt = seq[0]
     # >>> fn = lambda x,y: x + y
     # >>> accum = 0
     # >>> nxt = 1
     # >>> fn(accum, nxt)
     # 1
     #
     # >>> fn = lambda lst, x: lst + [x]
     # >>> accum = []
     # >>> nxt = 1
     # >>> fn(accum, nxt)
     [1]
     """

    if len(seq) == 0:
        return default

    nxt = first(seq)
    part_1 = fn(default, nxt)
    part_2 = rest(seq)

    res = my_reduce(fn, part_2, part_1)
    return res


def transfer_item(seq, item):
    """ return a new sequence that is the concatenation of sequence and item """
    res = seq + [item]
    return res


def summate_item(seq, item):
    """ return the sum of the sequence plus the item which is an integer """
    res = sum(seq) + item
    return res


#
# Script
#

def main():
    accum = [4, 5, 6]
    seq = seq = range(5)
    # #transf_ = transfer(accum, seq)
    # accum2 = 0
    # summmmate = summate(accum2, seq)
    lst_summate = summate_list(accum, seq)
    # print(find_recursion_limit())
    # print(iterative_transfer(accum, seq))
    print(iterative_summate_list(accum, seq))


# def test():
#     """ equiv to summate """
#     fn = lambda x, y: x + y
#     accum = 0
#     seq = range(5)
#     res = my_reduce(fn, seq, accum)
#     output = 10
#     assert res == output
#     print("test 1 success: {}".format(res))
#
#
# def test2():
#     """ equiv to transfer """
#
#     fn = lambda lst, x: lst + [x]
#     accum = []
#     seq = range(5)
#     res = my_reduce(fn, seq, accum)
#     output = [0, 1, 2, 3, 4]
#     assert res == output
#     print("test 2 success: {}".format(res))
#
#
# def test3():
#     """ equiv to summate_list """
#
#     def _summate_list(accum, nxt):
#         if len(accum) == 0:
#             res = [nxt]
#         else:
#             res = accum + [last(accum) + nxt]
#
#         return res
#
#     accum = []
#     seq = range(5)
#     res = my_reduce(_summate_list, seq, accum)
#     output = [0, 1, 3, 6, 10]
#     assert res == output
#     print("test 3 success: {}".format(res))


if __name__ == '__main__':
    main()
