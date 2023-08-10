#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    """ prints the sum of all arguments """
    arg_len = len(argv) - 1
    sum = 0

    if arg_len > 0:
        for i in range(arg_len):
            sum += int(argv[i + 1])

    print("{}".format(sum))
