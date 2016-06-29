###########
# Imports #
###########

from pprint import pprint

###########
# Library #
###########

def load_file(path):
    with open(path) as fhandle:
        res = fhandle.read()
        return res

def load_file_2(path):  # This is identical in function to the function above, but can be dangerous if the file being
                        # opened is corrupted.  The with function above has the try function built into it to avoid this.
    fhandle = open(path)
    res = fhandle.read()
    return res

def load_file_line(path):
    with open(path) as fhandle:
        for line in fhandle:
            yield line

def load_file_chunks(path, chunksize = 1024):
    with open(path) as fhandle:
        while True:
            nxt_chunk = fhandle.read(chunksize)
            if not nxt_chunk:
                raise StopIteration
            yield nxt_chunk


##########
# Script #
##########

def main():
    path = r"C:\Users\Coder\PycharmProjects\practice_work\my_tools\file_handling_rando.py"  #the r before the string
                                                                               # above stands for raw, so Python does
                                                                               # not interperet the backslashes as
                                                                               # escape characters.
    print(load_file(path))
    pprint(list(load_file_line(path)))
    pprint(list(load_file_chunks(path)))

if __name__ == '__main__':
    main()
