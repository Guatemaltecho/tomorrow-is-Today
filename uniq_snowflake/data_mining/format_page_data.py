###########
# Imports #
###########

import os


###########
# library #
###########

def open_file(path):
    with open(path) as fhandle:
        contents = fhandle.read()
        return contents


def file_with_split_lines(content):
    split_lines = content.split('\n\n')
    return split_lines


def create_list(split_lines):
    res = [x.rstrip('\n').split('\n') for x in split_lines[:-1]]
    return res


def get_dict_keys(lst):
    keys_ = [item for item in lst[0] if item != '']
    return keys_


def get_dict_values(lst):
    values_ = lst[1:]
    return values_


def list_of_dictionaries(keys_list, values_list):
    res = [dict(zip(keys_list, val_list)) for val_list in values_list]
    return res


##########
# script #
##########

def main():
    school_name = 'York College of Pennsylvania'
    file_name = school_name.replace(' ', '_')
    path = os.path.join('/Users/.../my_tools/data_mining',
                        '%s.txt' % file_name)
    funnel = reduce(lambda x, y: y(x), [open_file,file_with_split_lines,create_list], path)
    dictionary_of_class_info = list_of_dictionaries(get_dict_keys(funnel),get_dict_values(funnel))
    print(dictionary_of_class_info)


if __name__ == '__main__':
    main()
