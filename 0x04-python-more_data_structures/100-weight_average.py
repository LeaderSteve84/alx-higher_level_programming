#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sco = 0
    wgth = 0

    for i in my_list:
        sco += i[0] * i[1]
        wgth += i[1]

    return (sco / wgth)
