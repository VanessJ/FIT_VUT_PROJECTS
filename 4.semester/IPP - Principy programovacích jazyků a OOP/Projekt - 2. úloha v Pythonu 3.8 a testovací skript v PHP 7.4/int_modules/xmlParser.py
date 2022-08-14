"""
Brief:  IPP 2020/21 assigment - class that parses xml-source code
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""

import sys
import re

import xml.etree.ElementTree as ET
from int_modules.errorHandler import ErrorHandler
from int_modules.instruction import Instruction
from int_modules.instructionList import InstructionList
from int_modules.instructionArg import InstructionArg


class XMLParser:
    def __init__(self, xml_src, input_src):
        self.xml_src = xml_src
        self.input_src = input_src
        self.error_handler = ErrorHandler()
        self.inst_list = InstructionList()

    def parse_xml(self):
        """ Using ElementTree tries to parse the whole xml tree """
        if self.xml_src is None:
            self.xml_src = sys.stdin
        try:
            xml_tree = ET.parse(self.xml_src)
        except FileNotFoundError:
            self.error_handler.error_exit(11, "Cannot open XML source file")
        except ET.ParseError:
            self.error_handler.error_exit(
                31, "Bad XML formatting - cannot parse source file"
            )
        root = self.parse_root(xml_tree)
        self.parse_program(root)
        self.inst_list.order_instr()
        self.inst_list.get_labels()
        return self.inst_list

    def parse_root(self, xml_tree):
        """ Checks correctness of the root - root has to containt IPPcode21 atribute """
        root = xml_tree.getroot()
        if root.tag != "program":
            self.error_handler.error_exit(
                32, "Invalid XML root element - root element has to be program"
            )
        try:
            if not re.match("^ippcode21$", root.attrib["language"], re.IGNORECASE):
                self.error_handler.error_exit(
                    32, "Invalid value of attribute language - IPPcode21 is required"
                )
        except KeyError:
            self.error_handler.error_exit(32, "XML root does not have language element")

        for atr in root.attrib:
            if atr not in ["name", "language", "description"]:
                self.error_handler.error_exit(
                    32, "Invalid XML root atribute {}".format(atr)
                )

        return root

    def parse_program(self, root):
        """
        Checks if instruction has correct xml representation,
        builds instruction and appends Instruction List with given instruction
        """
        instruction_order = []
        for child in root:
            if child.tag != "instruction":
                self.error_handler.error_exit(
                    32,
                    "Invalid instruction tag {} - instruction tag has to be 'instruction'".format(
                        child.tag
                    ),
                )
            if "opcode" not in child.attrib or "order" not in child.attrib:
                self.error_handler.error_exit(
                    32,
                    "Invalid attributes of instruction {} - 'ocpode' or 'order' missing".format(
                        child
                    ),
                )

            # order, opcode check
            for attrib, value in child.attrib.items():
                if attrib == "opcode":
                    opcode = value.upper()
                if attrib == "order":
                    try:
                        if int(value) < 1:
                            self.error_handler.error_exit(
                                32,
                                "Invalid instruction order - order has to be greater than 0",
                            )
                    except ValueError:
                        self.error_handler.error_exit(
                            32, "Invalid instruction order - order has to be an integer"
                        )
                    order = int(value)
                    if order in instruction_order:
                        self.error_handler.error_exit(
                            32, "Instruction with duplicit order found"
                        )
                    else:
                        instruction_order.append(order)

            instruction_order.append(child.attrib["order"])

            arg_numbers = []
            arg_list = []
            for arg in child:
                if not re.match("arg[0-3]+", arg.tag, re.IGNORECASE):
                    self.error_handler.error_exit(
                        32,
                        "Invalid instruction argument format - only 'arg1' - 'arg3' are permitted",
                    )
                arg_num = int(arg.tag[3:])
                if arg_num in arg_numbers:
                    self.error_handler.error_exit(
                        32, "Instruction argument with duplicit order found"
                    )
                else:
                    arg_numbers.append(arg_num)
                    i_arg = InstructionArg(arg_num, arg.attrib["type"], arg.text)
                    arg_list.append(i_arg)

                if "type" not in arg.attrib:
                    self.error_handler.error_exit(
                        32, "'Type' attribute missing in instruction"
                    )
                if arg.attrib["type"] not in [
                    "int",
                    "string",
                    "bool",
                    "nil",
                    "type",
                    "var",
                    "label",
                    "float",
                ]:
                    self.error_handler.error_exit(
                        32,
                        "invalid instruction attribute type - {} is not supported".format(
                            arg.attrib["type"]
                        ),
                    )
            if 2 in arg_numbers and 1 not in arg_numbers:
                # only arg2 is present
                self.error_handler.error_exit(32, "Instriction arguments missing")
            if 3 in arg_numbers and (2 not in arg_numbers or 1 not in arg_numbers):
                # arg3 is present and arg2 or arg1 missing
                self.error_handler.error_exit(32, "Instriction arguments missing")
            new_i = Instruction(opcode, arg_list, order)
            new_i.check_instruction()
            self.inst_list.insert_instruction(new_i)
