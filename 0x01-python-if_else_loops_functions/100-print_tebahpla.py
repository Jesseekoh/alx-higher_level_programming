#!/usr/bin/python3
print_upper = False
for i in range(90, 64, -1):
    if print_upper:
        print("{}".format(chr(i)), end="")
        print_upper = False
    elif not print_upper:
        print("{}".format(chr(i + 32)), end="")
        print_upper = True
