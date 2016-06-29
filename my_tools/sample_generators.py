###########
# Library #
###########

def yield_too(n):
    i = 0
    while i < n:
        yield i
        i = i + 1

def yield_double_string(seq):
    for i in seq:
        res = (str(i) * 2)
        yield res

##########
# Script #
##########

def main():
    for item in yield_too(10):
        print(item)
    for item in yield_double_string([2, 3, 4, 5]):
        print(item)

if __name__ == '__main__':
    main()