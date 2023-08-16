#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0

    for a in my_list:
        num += a[0] * a[1]
        den += a[1]

    return (num / den)
