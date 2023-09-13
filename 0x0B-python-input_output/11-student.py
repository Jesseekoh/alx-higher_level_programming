#!/usr/bin/python3
"""
11-student module
"""


class Student:
    """
    class docs
    """
    def __init__(self, first_name, last_name, age):
        """
        initaialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json
        """
        my_list = {}
        all_string = True
        if type(attrs) is not list:
            all_string = False

        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    all_string = False
        if not all_string:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    my_list[i] = self.__dict__[i]
            return my_list

    def reload_from_json(self, json):
        """
        reload_from_json
        """
        for i in json:
            self.__dict__[i] = json[i]
