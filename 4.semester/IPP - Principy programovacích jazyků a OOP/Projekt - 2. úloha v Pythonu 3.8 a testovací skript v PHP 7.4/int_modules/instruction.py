"""
Brief:  IPP 2020/21 assigment - class that represents instruction 
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""


import re

from int_modules.errorHandler import ErrorHandler


class Instruction:
    """
    Class representing instruction consisting of opcode, order and arguments.
    Checks if internal representation represents correct instruction withou
    syntax or semantic errors.
    """

    def __init__(self, opcode, arg_list, order):
        self.opcode = opcode
        self.arg_count = 0
        self.arg_list = arg_list
        self.order = order
        self.real_order = None
        for arg in arg_list:
            if arg.number == 1:
                self.arg1 = arg
                self.arg_count += 1
            if arg.number == 2:
                self.arg2 = arg
                self.arg_count += 1
            if arg.number == 3:
                self.arg3 = arg
                self.arg_count += 1
        error_handler = ErrorHandler()
        self.error_handler = error_handler

    def check_instruction(self):
        """
        Checks correctness of instruction based on opcode, number of arguments and arguments types
        """
        if self.opcode in ["CREATEFRAME", "POPFRAME", "PUSHFRAME", "RETURN", "BREAK"]:
            self.check_arg_nmbr(0, self.arg_count)
        elif self.opcode in ["LABEL", "JUMP", "CALL", "JUMPIFEQS", "JUMPIFNEQS"]:
            # opcode <label>
            self.check_arg_nmbr(1, self.arg_count)
            self.check_label(self.arg1)
        elif self.opcode in ["DEFVAR", "POPS"]:
            # opcode <var>
            self.check_arg_nmbr(1, self.arg_count)
            self.check_var(self.arg1)
        elif self.opcode in ["PUSHS", "WRITE", "EXIT", "DPRINT"]:
            # opcode <symb>
            self.check_arg_nmbr(1, self.arg_count)
            self.check_symbol(self.arg1)
        elif self.opcode in [
            "MOVE",
            "STRLEN",
            "TYPE",
            "NOT",
            "INT2CHAR",
            "INT2FLOAT",
            "FLOAT2INT",
        ]:
            # opcode <var> <symb>
            self.check_arg_nmbr(2, self.arg_count)
            self.check_var(self.arg1)
            self.check_symbol(self.arg2)
        elif self.opcode in ["READ"]:
            # opcode <var> <type>
            self.check_arg_nmbr(2, self.arg_count)
            self.check_var(self.arg1)
            self.check_type(self.arg2)
        elif self.opcode in [
            "ADD",
            "SUB",
            "MUL",
            "IDIV",
            "DIV",
            "LT",
            "GT",
            "EQ",
            "AND",
            "OR",
            "STRI2INT",
            "CONCAT",
            "GETCHAR",
            "SETCHAR",
        ]:
            # opcode <var> <symb> <symb>
            self.check_arg_nmbr(3, self.arg_count)
            self.check_var(self.arg1)
            self.check_symbol(self.arg2)
            self.check_symbol(self.arg3)

        elif self.opcode in ["JUMPIFEQ", "JUMPIFNEQ"]:
            # opcode <label> <symb> <symb>
            self.check_arg_nmbr(3, self.arg_count)
            self.check_label(self.arg1)
            self.check_symbol(self.arg2)
            self.check_symbol(self.arg3)

        elif self.opcode in [
            "CLEARS",
            "ADDS",
            "SUBS",
            "MULS",
            "IDIVS",
            "LTS",
            "GTS",
            "EQS",
            "ANDS",
            "ORS",
            "NOTS",
            "INT2CHARS",
            "STRI2INTS",
        ]:
            self.check_arg_nmbr(0, self.arg_count)
        else:
            self.error_handler.error_exit(
                32, "Unsupported opcode {} of instruction".format(self.opcode)
            )

    def check_arg_nmbr(self, expected, actual):
        """
        Checks if instruction argument number corresponds to expected argument number
        """
        if expected != actual:
            self.error_handler.error_exit(
                32, "Invalid number of arguments in {} instruction".format(self.opcode)
            )

    def check_var(self, arg):
        """ Checks if variable argument is correct """
        if arg.arg_type != "var":
            self.error_handler.error_exit(
                32,
                "Invalid argument type {} in {} instruction".format(
                    arg.arg_type, self.opcode
                ),
            )
        if not re.match(
            "^(GF|LF|TF)@[a-zA-Z_\-$&%*!?][0-9a-zA-Z_\-$&%*!?]*$", arg.text
        ):
            self.error_handler.error_exit(
                32,
                "Invalid argument {} in {} instruction".format(arg.text, self.opcode),
            )

    def check_label(self, arg):
        """ Checks if label argument is correct """
        if arg.arg_type != "label":
            self.error_handler.error_exit(
                32,
                "Invalid argument type '{}' in {} instruction".format(
                    arg.arg_type, self.opcode
                ),
            )
        if not re.match("^[a-zA-Z_\-$&%*!?][0-9a-zA-Z_\-$&%*!?]*$", arg.text):
            self.error_handler.error_exit(
                32,
                "Invalid argument '{}' in {} instruction".format(arg.text, self.opcode),
            )

    def check_type(self, arg):
        """ Checks if type argument is correct """
        if arg.arg_type != "type":
            self.error_handler.error_exit(
                32,
                "Invalid argument type '{}' in {} instruction".format(
                    arg.arg_type, self.opcode
                ),
            )
        if not re.match("^(string|int|bool|float)$", arg.text):
            self.error_handler.error_exit(
                32,
                "Invalid argument '{}' in {} instruction".format(arg.text, self.opcode),
            )

    def check_symbol(self, arg):
        """ Checks if symbol argument is correct """
        if arg.arg_type == "var":
            self.check_var(arg)
        elif arg.arg_type in ["int", "bool", "string", "nil", "float"]:
            if arg.arg_type == "int":
                if not re.match("^[+-]?\d+$", arg.text):
                    self.error_handler.error_exit(
                        32,
                        "Invalid argument '{}' in {} instruction".format(
                            arg.text, self.opcode
                        ),
                    )
            elif arg.arg_type == "bool":
                if not re.match("^(true|false)$", arg.text):
                    self.error_handler.error_exit(
                        32,
                        "Invalid argument '{}' in {} instruction".format(
                            arg.text, self.opcode
                        ),
                    )
            elif arg.arg_type == "string":
                if arg.text is None:
                    arg.text = ""

                elif not re.match(
                    "^(\\\\[0-9]{3}|[^\s\\\\#])*$",
                    arg.text,
                ):
                    self.error_handler.error_exit(
                        32,
                        "Invalid argument '{}' in {} instruction".format(
                            arg.text, self.opcode
                        ),
                    )

                arg.text = re.sub(
                    r"\\([0-9]{3})", lambda x: chr(int(x.group(1))), arg.text
                )

            elif arg.arg_type == "nil":
                if not re.match("^nil$", arg.text):
                    self.error_handler.error_exit(
                        32,
                        "Invalid argument '{}' in {} instruction".format(
                            arg.text, self.opcode
                        ),
                    )

            elif arg.arg_type == "float":
                try:
                    convert = float.fromhex(arg.text)
                    arg.text = convert
                except (ValueError, TypeError):
                    self.error_handler.error_exit(
                        32,
                        "Invalid argument '{}' in {} instruction".format(
                            arg.text, self.opcode
                        ),
                    )
