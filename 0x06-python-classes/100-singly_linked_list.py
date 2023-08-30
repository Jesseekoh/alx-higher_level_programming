#!/usr/bin/python3
"""
    Node class
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.getter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(selft, value):
        if type(value) is not Node or value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node.data < value and node.next_node is not None:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
