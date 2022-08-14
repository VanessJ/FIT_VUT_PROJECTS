"""
Brief:  IPP 2020/21 assigment - class representation of isntruction list
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""


from int_modules.errorHandler import ErrorHandler


class InstructionList:
    """" Class representation of instruction list consisting of ordered instructions and program counter """

    def __init__(self):
        self.unordered = []
        self.ordered = []
        self.labels = {}
        self.PC = 1
        self.inst_count = 0
        self.error_handler = ErrorHandler()

    def insert_instruction(self, instruction):
        """ Adds instruction to instruction list """
        self.unordered.append(instruction)

    def print_instr(self):
        """ Debuging method - prints unordered instrustion list """
        for ins in self.unordered:
            print("{} {}".format(ins.opcode, ins.order))

    def print_ordered(self):
        """ Debuging method - prints ordered instrustion list """
        for ins in self.ordered:
            print("{} {}".format(ins.opcode, ins.order))

    def order_instr(self):
        """ Sorts instruction to create ordered instruction list """
        self.ordered = sorted(self.unordered, key=lambda i: int(i.order))
        order = 1
        for i in self.ordered:
            i.real_order = order
            order += 1
            # print("{} {}, {}".format(i.opcode, i.order, i.real_order))
        self.inst_count = len(self.ordered)

    def get_labels(self):
        """
        Creates dict with all labels and their respective position in code to facilitate JUMP instructions
        """
        for i in self.ordered:
            if i.opcode == "LABEL":
                if not i.arg1.text in self.labels:
                    self.labels[i.arg1.text] = i
                else:
                    self.error_handler.error_exit(
                        52, "Label {} already exists".format(i.arg1.text)
                    )

    def get_inst(self):
        """
        Returns instruction on position corresponding to current program counter value
        and increases program counter value
        Return None if the end of instruction list is reached
        """
        if (self.PC) > self.inst_count:
            return None
        else:
            inst = self.ordered[self.PC - 1]
            self.PC += 1
            return inst

    def set_PC(self, number):
        """ Sets program counter as specific value """
        self.PC = number

    def get_PC(self):
        """ Returns current program counter value """
        return self.PC