###########
# Imports #
###########

import re


###########
# Library #
###########

def word_counter(source_data):
    """counts the frequency of each word in a document"""
    word_count_map = {}
    source_data = source_data.lower()
    tokens = re.split('([a-z]+)', source_data)

    for token in tokens:
        word_count_map[token] = tokens.count(token)

    word_count_array = sorted(word_count_map.items(), key=lambda t:t[1])
    word_count_array_highest_first = word_count_array[::-1]

    return word_count_array_highest_first


##########
# Script #
##########

def main():
    test_input = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""
    print word_counter(test_input)

if __name__ == '__main__':
    main()