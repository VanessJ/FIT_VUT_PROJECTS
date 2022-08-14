"""
Brief:  IPP 2020/21 assigment - class representation of isntruction argument
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""


class InstructionArg:
    """
    Representation of instruction argument containing number, type and text (value)
    """

    def __init__(self, number, arg_type, text):
        self.number = number
        self.arg_type = arg_type
        self.text = text
