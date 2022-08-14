"""
Brief:  IPP 2020/21 assigment - Interpret of IPPcode21
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""


import sys
from int_modules.argParser import ArgParser
from int_modules.xmlParser import XMLParser
from int_modules.instructionList import InstructionList
from int_modules.interpretCode import InterpetCode

# process arguments
arg_parser = ArgParser()
arg_src, arg_input, arg_stats = arg_parser.get_and_chech_args()

# parse source file XML structure
xml_parser = XMLParser(arg_src, arg_input)
inst_list = InstructionList()
inst_list = xml_parser.parse_xml()

# interpret given code
interpretCode = InterpetCode(inst_list, arg_input, arg_stats)
interpretCode.interpret()
sys.exit(0)
