"""
Brief:  IPP 2020/21 assigment - class representation of variable 
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""
TYPE_NIL = 11
TYPE_BOOL = 12
TYPE_INT = 13
TYPE_STRING = 14
TYPE_FLOAT = 15


class Variable:
    """
    Representation of variable containing name of the variable and type and valued (if inicialized)
    """

    def __init__(self, name):
        self.name = name
        self.type = None
        self.value = None