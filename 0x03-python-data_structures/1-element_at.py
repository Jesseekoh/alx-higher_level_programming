#!/usr/bin/python3
def element_at(my_list, idx):
    """Gets element at a given index of a specified list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None

    return (my_list[idx])
