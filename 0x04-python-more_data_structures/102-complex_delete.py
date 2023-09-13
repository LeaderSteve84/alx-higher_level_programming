#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())

    for n in keys_list:
        if value == a_dictionary.get(n):
            del a_dictionary[n]

    return (a_dictionary)
