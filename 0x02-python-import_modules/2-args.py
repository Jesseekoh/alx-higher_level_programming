#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv) - 1
    if arg_len == 1:
        print("{} argument:".format(arg_len))
    elif arg_len > 2:
        print("{} arguments:".format(arg_len))
    else:
        print("{} arguments.".format(0))

    for i in range(len(argv)):
        if i > 0:
            print("{}: {}".format(i, argv[i]))
