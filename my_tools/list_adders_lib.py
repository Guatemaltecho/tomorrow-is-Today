###########
# Library #
###########

def list_add_one(lst):
    res = []
    for num in lst:
      res.append(num + 1)
    return res


def add_1_to_list_2(lst):
    for i in range(len(lst)):
        lst[i] += 1
    return lst


def add_one_lst_comprehension(lst):
    res = (x + 1 for x in lst)
    return list(res)


def plus_one(x):
    return x + 1


def map_plus_one(lst):
    return map(plus_one, lst)


def add_n_to_list(n, lst):            # general function
    return map(lambda x: x + n, lst)

def add_one_to_list_spec(lst):        # specific implementatin of general function
    return add_n_to_list(1, lst)


def is_divisible_by(num, lst):
    return filter(lambda x: x % num == 0, lst)

def get_even_number_spec(lst):
    return is_divisible_by(2, lst)