"""
Brief:  IPP 2020/21 assigment - main class responsible of interpretation of programs
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
Details:    XML representation of program is converted to ordered Instruction List
            consisting of object representation of specific instructions and their 
            arguments.
            Given isntructions are interpreted from start to finish with the support of JUMP
            instructions.
            All created variables are stored on various frames. 
"""


import re
import sys
from int_modules.instructionList import InstructionList
from int_modules.instruction import Instruction
from int_modules.errorHandler import ErrorHandler
from int_modules.frames import Frames
from int_modules.variable import Variable

TYPE_NIL = 11
TYPE_BOOL = 12
TYPE_INT = 13
TYPE_STRING = 14
TYPE_FLOAT = 15
DEBUG = False


class InterpetCode:
    """
    Class responsible for code interpretation.
    Supporting structures:
    Frames as memory model.
    Stack storing call values for correct return from function. 
    Data stack simulating stack for stack instructions. 
    Stat_list for storing statistics of program.
    
    """
    def __init__(self, inst_list, arg_input, arg_stats):
        self.inst_list = inst_list
        self.calls = []
        self.error_handler = ErrorHandler()
        self.frames = Frames()
        self.data_stack = []
        self.input = arg_input
        self.arg_stats = arg_stats
        self.read = None
        self.stat_list = []
        self.max_vals = 0
        self.inst_amount = 0

    def interpret(self):
        """
        Interprets instructions from instruction-list from start to finish 
        with support of JUMP instructions.
        Based on opcode-value chooses corresponding method of instruction interpretation.
        """
        # self.inst_list.print_ordered()
        if self.input is not None:
            try:
                file = open(self.input, "r")
                self.read = file.readlines()
                file.close()
            except IOError:
                self.error_handler.error_exit(11, "Unable to open input file")
        while 1:
            inst = self.inst_list.get_inst()
            if inst is None:
                break

            if inst.opcode != "LABEL" and inst.opcode != "DPRINT" and inst.opcode != "BREAK":
                self.inst_amount += 1
            self.statlist_add(inst)
            self.count_vars()


            if inst.opcode == "MOVE":
                self.interpret_move(inst)
            elif inst.opcode == "CREATEFRAME":
                self.interpret_createframe(inst)
            elif inst.opcode == "PUSHFRAME":
                self.interpret_pushframe(inst)
            elif inst.opcode == "POPFRAME":
                self.interpret_popframe(inst)
            elif inst.opcode == "DEFVAR":
                self.interpret_defvar(inst)
            elif inst.opcode == "CALL":
                self.interpret_call(inst)
            elif inst.opcode == "RETURN":
                self.interpret_return(inst)
            elif inst.opcode == "PUSHS":
                self.interpret_pushs(inst)
            elif inst.opcode == "POPS":
                self.interpret_pops(inst)
            elif inst.opcode == "ADD":
                self.interpret_add(inst)
            elif inst.opcode == "SUB":
                self.interpret_sub(inst)
            elif inst.opcode == "MUL":
                self.interpret_mul(inst)
            elif inst.opcode == "DIV":
                self.interpret_div(inst)
            elif inst.opcode == "IDIV":
                self.interpret_idiv(inst)
            elif inst.opcode == "LT":
                self.interpret_lt(inst)
            elif inst.opcode == "GT":
                self.interpret_gt(inst)
            elif inst.opcode == "EQ":
                self.interpret_eq(inst)
            elif inst.opcode == "AND":
                self.interpret_and(inst)
            elif inst.opcode == "OR":
                self.interpret_or(inst)
            elif inst.opcode == "NOT":
                self.interpret_not(inst)
            elif inst.opcode == "INT2CHAR":
                self.interpret_int2char(inst)
            elif inst.opcode == "STRI2INT":
                self.interpret_stri2int(inst)
            elif inst.opcode == "WRITE":
                self.interpret_write(inst)
            elif inst.opcode == "READ":
                self.interpret_read(inst)
            elif inst.opcode == "CONCAT":
                self.interpret_concat(inst)
            elif inst.opcode == "STRLEN":
                self.interpret_strlen(inst)
            elif inst.opcode == "SETCHAR":
                self.interpret_setchar(inst)
            elif inst.opcode == "GETCHAR":
                self.interpret_getchar(inst)
            elif inst.opcode == "TYPE":
                self.interpret_type(inst)
            elif inst.opcode == "LABEL":
                self.interpret_label(inst)
            elif inst.opcode == "JUMP":
                self.interpret_jump(inst)
            elif inst.opcode == "JUMPIFEQ":
                self.interpret_jumpifeq(inst)
            elif inst.opcode == "JUMPIFNEQ":
                self.interpret_jumpifneq(inst)
            elif inst.opcode == "EXIT":
                number = self.interpret_exit(inst)
                if self.arg_stats is not None:
                    self.write_stats()
                sys.exit(number)
            elif inst.opcode == "DPRINT":
                self.interpret_dprint(inst)
            elif inst.opcode == "BREAK":
                self.interpret_break(inst)
            elif inst.opcode == "CLEARS":
                self.interpret_clears()
            elif inst.opcode == "ADDS":
                self.interpret_adds(inst)
            elif inst.opcode == "SUBS":
                self.interpret_subs(inst)
            elif inst.opcode == "MULS":
                self.interpret_muls(inst)
            elif inst.opcode == "IDIVS":
                self.interpret_idivs(inst)
            elif inst.opcode == "LTS":
                self.interpret_lts(inst) 
            elif inst.opcode == "GTS":
                self.interpret_gts(inst) 
            elif inst.opcode == "EQS":
                self.interpret_eqs(inst) 
            elif inst.opcode == "ANDS":
                self.interpret_ands(inst) 
            elif inst.opcode == "ORS":
                self.interpret_ors(inst) 
            elif inst.opcode == "NOTS":
                self.interpret_nots(inst)
            elif inst.opcode == "INT2CHARS":
                self.interpret_int2chars(inst)
            elif inst.opcode == "STRI2INTS":
                self.interpret_stri2ints(inst) 
            elif inst.opcode == "JUMPIFEQS":
                self.interpret_jumpifeqs(inst)
            elif inst.opcode == "JUMPIFNEQS":
                self.interpret_jumpifneqs(inst)   
            elif inst.opcode == "INT2FLOAT":
                self.interpret_int2float(inst)  
            elif inst.opcode == "FLOAT2INT":
                self.interpret_float2int(inst)    
            else:
                print("Zlá instrukcia - sem by som sa nemala dostat")
        if self.arg_stats is not None:
            self.write_stats()

            
            
    def write_stats(self):
        """
        STATI extension - based on program args writes stats to given file
        """
        try:
            file = open(self.arg_stats, "w+")
        except IOError:
            self.error_handler.error_exit(11, "Unable to open input file")
        for arg in sys.argv:
            if arg == "--insts":
                file.write(str(self.inst_amount) + "\n")
            if arg == "--vars":
                file.write(str(self.max_vals)+ "\n")
            if arg == "--hot":
                s_max = self.statlist_find_max()
                file.write(str(s_max[1])+ "\n")



    def statlist_add(self, inst):
        """ STATI expansion - function collecting program statistics """
        # [opcode, first_order, amount]
        found = False
        if inst.opcode == "DPRINT" or inst.opcode == "LABEL" or inst.opcode == "BREAK":
            return
        for stats in self.stat_list:
            if stats[0] == inst.opcode:
                found = True
                stats[2] += 1 
                if stats[1] > inst.real_order:
                    stats[1] = inst.real_order
        if not found:
            self.stat_list.append([inst.opcode, inst.real_order, 1])

    def statlist_find_max(self):
        """ 
        STATI expansion - function returning most executed isntruction   
        """
        s_max = ["Placeholder", 1, 0]
        for stats in self.stat_list:
            if stats[2] > s_max[2]:
                s_max = stats
            elif stats[2] == s_max[2]:
                if stats[1] < s_max[1]:
                    s_max = stats
        if s_max[2] == 0:
            return None
        else:
            return s_max

    def count_vars(self):
        """
        STATI expansion - count inicialized variables on frames at given time 
        """
        GF_vars = 0
        TF_vars = 0
        stack_vars = 0
        if self.frames.global_frame is not None:
            for var in self.frames.global_frame:
                if var.type is not None:
                    GF_vars +=1
        if self.frames.temp_frame is not None:
            for var in self.frames.temp_frame:
                if var.type is not None:
                    TF_vars +=1
        for frame in self.frames.frame_stack:
            for var in frame:
                if var.type is not None:
                    stack_vars += 1
        count = GF_vars + TF_vars + stack_vars
        if count > self.max_vals:
            self.max_vals = count


    ### INTERPRETATION OF INSTRUCTIONS ### 

    # <var> <symb>
    def interpret_move(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        varname = inst.arg1.text
        var = self.get_var(varname, False)
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        var.value = arg2_value
        var.type = arg2_type

    def interpret_createframe(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        self.frames.temp_frame = []

    def interpret_pushframe(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        self.frames.push_frame()

    def interpret_popframe(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        self.frames.pop_frame()

    # <var>
    def interpret_defvar(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        frame, name = re.split("@", inst.arg1.text)
        var = Variable(name)
        if frame == "GF":
            self.frames.add_to_GF(var)
        if frame == "LF":
            self.frames.add_to_LF(var)
        if frame == "TF":
            self.frames.add_to_TF(var)

    def interpret_call(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )
        counter = self.inst_list.get_PC()
        self.calls.append(counter)
        self.inst_list.set_PC(inst_l.real_order)

    def interpret_return(self, inst):
        if len(self.calls) < 1:
            self.error_handler.error_exit(56, "Invalid return call")
        else:
            counter = self.calls.pop()
            self.inst_list.set_PC(counter)

    # <symb>
    def interpret_pushs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_value, stack_type = self.get_symbol(inst.arg1, True)
        self.data_stack.append([stack_value, stack_type])

    # <symb>
    def interpret_pops(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        varname = inst.arg1.text
        var = self.get_var(varname, False)
        if len(self.data_stack) < 1:
            self.error_handler.error_exit(56, "Attempting POPS with empty data stack")
        var.value, var.type = self.data_stack.pop()

    # <var> <symb> <symb>
    def interpret_add(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var_type, op_1, op_2 = self.arithmetic_operation_check(inst)
        var.type = var_type
        if var_type == TYPE_INT:
            var.value = int(op_1) + int(op_2)
        elif var_type == TYPE_FLOAT:
            var.value = float(op_1) + float(op_2)

    # <var> <symb> <symb>
    def interpret_sub(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type, op_1, op_2 = self.arithmetic_operation_check(inst)
        if var.type == TYPE_INT:
            var.value = int(op_1) - int(op_2)
        elif var.type == TYPE_FLOAT:
            var.value = float(op_1) - float(op_2)

    # <var> <symb> <symb>
    def interpret_mul(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type, op_1, op_2 = self.arithmetic_operation_check(inst)
        if var.type == TYPE_INT:
            var.value = int(op_1) * int(op_2)
        elif var.type == TYPE_FLOAT:
            var.value = float(op_1) * float(op_2)

    # <var> <symb> <symb>
    def interpret_idiv(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type, op_1, op_2 = self.arithmetic_operation_check(inst)
        division = int(op_1) // int(op_2)
        var.value = int(division)

    def interpret_div(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type, op_1, op_2 = self.arithmetic_operation_check(inst)
        division = float(op_1) / float(op_2)
        var.value = float(division)

    # <var> <symb> <symb>
    def interpret_lt(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.relation_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        var.type = TYPE_BOOL
        if op_1 < op_2:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb> <symb>
    def interpret_gt(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.relation_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        var.type = TYPE_BOOL
        if op_1 > op_2:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb> <symb>
    def interpret_eq(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.relation_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        op_1, op_2 = self.convert_nil(op_1, op_2)
        var.type = TYPE_BOOL
        if op_1 == op_2:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb> <symb>
    def interpret_and(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.logical_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        var.type = TYPE_BOOL
        if op_1 and op_2:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb> <symb>
    def interpret_or(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.logical_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        var.type = TYPE_BOOL
        if op_1 or op_2:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb>
    def interpret_not(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        op_1, op_2 = self.logical_operation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        var.type = TYPE_BOOL
        if not op_1:
            var.value = "true"
        else:
            var.value = "false"

    # <var> <symb>
    def interpret_int2char(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_STRING
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        if arg2_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "Second operand of int2char must be of type INT"
            )
        int_value = int(arg2_value)
        try:
            var.value = chr(int_value)
        except ValueError:
            self.error_handler.error_exit(58, "Cannot convert int value to char")

    # <var> <symb> <symb>
    def interpret_stri2int(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_INT
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        if arg2_type != TYPE_STRING:
            self.error_handler.error_exit(
                53, "Second operand of STRI2INT must be of type STRING"
            )
        string = arg2_value
        if arg3_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "Second operand of STRI2INT must be of type STRING"
            )
        position = int(arg3_value)

        if position < 0 or position > len(string) - 1:
            self.error_handler.error_exit(58, "STRI2INT - Index out of bounds")
        var.value = ord(string[position])

    # <var> <type>
    def interpret_read(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        if inst.arg2.arg_type != "type":
            self.error_handler.error_exit(53, "READ - second operand is not TYPE")
        read_type = inst.arg2.text
        if self.input is None:
            try:
                read_value = input()
            except (KeyboardInterrupt, EOFError):
                read_value = None
        else:
            try:
                read_value = self.read.pop(0)
            except (IndexError, EOFError):
                read_value = None

        if read_value is None:
            var.type = TYPE_NIL
            var.value = "nil"
        elif read_type == "int":
            try:
                var.type = TYPE_INT
                var.value = int(read_value)
            except (ValueError, TypeError):
                var.type = TYPE_NIL
                var.value = "nil"
        elif read_type == "float":
            try:
                var.type = TYPE_FLOAT
                var.value = float.fromhex(read_value)
            except (ValueError, TypeError):
                var.type = TYPE_NIL
                var.value = "nil"
        elif read_type == "string":
            var.type = TYPE_STRING
            var.value = read_value
        elif read_type == "bool":
            read_value = str(read_value).lower()
            if read_value == "true":
                read_value = "true"
            else:
                read_value = "false"
            var.type = TYPE_BOOL
            var.value = read_value

    # <symbol>
    def interpret_write(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        if inst.arg1.arg_type == "var":
            var = self.get_var(inst.arg1.text, True)
            if var.value is None:
                self.error_handler.error_exit(
                    56, "WRITE - trying to print variable with no value"
                )
            if var.type == TYPE_NIL:
                to_print = ""
            elif var.type == TYPE_FLOAT:
                to_print = str(float.hex(var.value))

            else:
                to_print = var.value

        else:
            arg_type = self.get_type(inst.arg1.arg_type)
            if arg_type == TYPE_NIL:
                to_print = ""
            elif arg_type == TYPE_FLOAT:
                to_print = str(float.hex(inst.arg1.text))
            else:
                to_print = inst.arg1.text
        print(to_print, end="")

    # <var> <symbol> <symbol>
    def interpret_concat(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_STRING
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        if arg2_type != TYPE_STRING or arg3_type != TYPE_STRING:
            self.error_handler.error_exit(
                53, "Both operands of CONCAT must be of type STRING"
            )
        string1 = arg2_value
        string2 = arg3_value

        var.value = string1 + string2

    # <var> <symb>
    def interpret_strlen(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_INT
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        if arg2_type != TYPE_STRING:
            self.error_handler.error_exit(
                53, "Second operand of STRLEN must be of type STRING"
            )
        string = arg2_value

        var.value = len(string)

    # <var> <symb> <symb>
    def interpret_getchar(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_STRING

        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        if arg2_type != TYPE_STRING:
            self.error_handler.error_exit(
                53, "Second operand of GETCHAR must be of type STRING"
            )
        string = arg2_value
        if arg3_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "THIRD operand of GETCHAR must be of type INT"
            )
        position = int(arg3_value)

        if position < 0 or position > len(string) - 1:
            self.error_handler.error_exit(58, "GETCHAR - Index out of bounds")
        var.value = string[position]

    def interpret_setchar(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, True)
        if var.type != TYPE_STRING:
            self.error_handler.error_exit(53, "SETCHAR - value of var is not STRING")
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        if arg2_type != TYPE_INT:
            self.error_handler.error_exit(53,
                "SETCHAR - type of second operand must be INT"
            )
        if arg3_type != TYPE_STRING:
            self.error_handler.error_exit(53,
                "SETCHAR - type of third operand must be STRING"
            )

        if len(arg3_value) < 1:
            self.error_handler.error_exit(
                58, "SETCHAR - Argument 3 cant be empty string"
            )

        string = var.value
        position = int(arg2_value)
        char = arg3_value[0]

        if position < 0 or position > len(var.value) - 1:
            self.error_handler.error_exit(58, "SETCHAR - Index out of bounds")

        changed = string[:position] + char + string[position + 1 :]
        var.value = changed

    def interpret_type(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        arg2_value, arg2_type = self.get_symbol(inst.arg2, False)
        if arg2_value is None or arg2_type is None:
            string_value = ""
        elif arg2_type == TYPE_INT:
            string_value = "int"
        elif arg2_type == TYPE_FLOAT:
            string_value = "float"
        elif arg2_type == TYPE_STRING:
            string_value = "string"
        elif arg2_type == TYPE_BOOL:
            string_value = "bool"
        elif arg2_type == TYPE_NIL:
            string_value = "nil"
        else:
            string_value = "nejaka blbost"
        var.value = string_value
        var.type = TYPE_STRING

    def interpret_label(self, inst):
        pass

    def interpret_jump(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )
        self.inst_list.set_PC(inst_l.real_order)

    def interpret_jumpifeq(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        jump = False
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        arg2_value, arg3_value = self.convert_bool(arg2_value, arg3_value)
        arg2_value, arg3_value = self.convert_nil(arg2_value, arg3_value)

        if arg2_type != TYPE_NIL and arg3_type != TYPE_NIL:
            if arg2_type != arg3_type:
                self.error_handler.error_exit(
                    53, "JUMPIFEQ has operands of different types"
                )

            if arg2_type == TYPE_INT:
                arg2_value = int(arg2_value)
                arg3_value = int(arg3_value)

            if arg2_type == TYPE_FLOAT:
                arg2_value = float(arg2_value)
                arg3_value = float(arg3_value)

        if arg2_value == arg3_value:
            jump = True

        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )
            
        if jump:
            self.inst_list.set_PC(inst_l.real_order)

    def interpret_jumpifneq(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        jump = False
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        arg3_value, arg3_type = self.get_symbol(inst.arg3, True)
        arg2_value, arg3_value = self.convert_bool(arg2_value, arg3_value)
        arg2_value, arg3_value = self.convert_nil(arg2_value, arg3_value)

        if arg2_type != TYPE_NIL and arg3_type != TYPE_NIL:
            if arg2_type != arg3_type:
                self.error_handler.error_exit(
                    53, "JUMPIFEQ has operands of different types"
                )

            if arg2_type == TYPE_INT:
                arg2_value = int(arg2_value)
                arg3_value = int(arg3_value)

            if arg2_type == TYPE_FLOAT:
                arg2_value = float(arg2_value)
                arg3_value = float(arg3_value)

        if arg2_value != arg3_value:
            jump = True

        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )

        if jump:
            self.inst_list.set_PC(inst_l.real_order)

    def interpret_dprint(self, inst):
        pass

    def interpret_break(self, inst):
        pass

    def interpret_exit(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        arg1_value, arg1_type = self.get_symbol(inst.arg1, True)
        if arg1_type != TYPE_INT:
            self.error_handler.error_exit(53, "Argument of EXIT has to be of type INT")
        number = int(arg1_value)
        if number < 0 or number > 49:
            self.error_handler.error_exit(57, "Invalid EXIT number value")
        return number


    ### FLOAT ###

    def interpret_int2float(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_FLOAT
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        if arg2_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "Second operand of int2float must be of type INT"
            )
        int_value = int(arg2_value)
        var.value = float(int_value)


    def interpret_float2int(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        var = self.get_var(inst.arg1.text, False)
        var.type = TYPE_INT
        arg2_value, arg2_type = self.get_symbol(inst.arg2, True)
        if arg2_type != TYPE_FLOAT:
            self.error_handler.error_exit(
                53, "Second operand of float2int must be of type INT"
            )
        float_value = float(arg2_value)
        var.value = int(float_value)

    

    ### STACK ###

    def interpret_clears(self):
        self.data_stack = []

    def interpret_adds(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_type, op_1, op_2 = self.stack_arithmetic_check(inst)
        if stack_type == TYPE_INT:
            stack_value = int(op_1) + int(op_2)
        elif stack_type == TYPE_FLOAT:
            stack_value = float(op_1) + float(op_2)
        self.data_stack.append([stack_value, stack_type])

    def interpret_subs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_type, op_1, op_2 = self.stack_arithmetic_check(inst)
        if stack_type == TYPE_INT:
            stack_value = int(op_1) - int(op_2)
        elif stack_type == TYPE_FLOAT:
            stack_value = float(op_1) - float(op_2)
        self.data_stack.append([stack_value, stack_type])

    def interpret_muls(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_type, op_1, op_2 = self.stack_arithmetic_check(inst)
        if stack_type == TYPE_INT:
            stack_value = int(op_1) * int(op_2)
        elif stack_type == TYPE_FLOAT:
            stack_value = float(op_1) * float(op_2)
        self.data_stack.append([stack_value, stack_type])

    def interpret_idivs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_type, op_1, op_2 = self.stack_arithmetic_check(inst)
        stack_value = int(op_1) // int(op_2)
        self.data_stack.append([stack_value, stack_type])


    def interpret_lts(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_relation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        stack_type = TYPE_BOOL
        if op_1 < op_2:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    def interpret_gts(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_relation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        stack_type = TYPE_BOOL
        if op_1 > op_2:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    def interpret_eqs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_relation_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        op_1, op_2 = self.convert_nil(op_1, op_2)
        stack_type = TYPE_BOOL
        if op_1 == op_2:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    def interpret_ands(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_logical_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        stack_type = TYPE_BOOL
        if op_1 and op_2:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    def interpret_ors(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_logical_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        stack_type = TYPE_BOOL
        if op_1 or op_2:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    def interpret_nots(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        op_1, op_2 = self.stack_logical_check(inst)
        op_1, op_2 = self.convert_bool(op_1, op_2)
        stack_type = TYPE_BOOL
        if not op_1:
            stack_value = "true"
        else:
            stack_value = "false"
        self.data_stack.append([stack_value, stack_type])

    
    def interpret_int2chars(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        if len(self.data_stack) < 1:
            self.error_handler.error_exit(56, "Missing value on stack")
        stack_type = TYPE_STRING
        arg2_value, arg2_type = self.data_stack.pop()
        if arg2_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "Second operand of int2char must be of type INT"
            )
        int_value = int(arg2_value)
        try:
            stack_value = chr(int_value)
        except ValueError:
            self.error_handler.error_exit(58, "Cannot convert int value to char")
        self.data_stack.append([stack_value, stack_type])


    def interpret_stri2ints(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        stack_type = TYPE_INT

        arg2_value, arg3_value, arg2_type, arg3_type = self.stack_get_operands()

        if arg2_type != TYPE_STRING:
            self.error_handler.error_exit(
                53, "Second operand of STRI2INT must be of type STRING"
            )
        string = arg2_value
        if arg3_type != TYPE_INT:
            self.error_handler.error_exit(
                53, "Second operand of STRI2INT must be of type STRING"
            )
        position = int(arg3_value)

        if position < 0 or position > len(string) - 1:
            self.error_handler.error_exit(58, "STRI2INT - Index out of bounds")
        stack_value = ord(string[position])
        self.data_stack.append([stack_value, stack_type])


    def interpret_jumpifeqs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        jump = False
        arg2_value, arg3_value, arg2_type, arg3_type = self.stack_get_operands()
        arg2_value, arg3_value = self.convert_bool(arg2_value, arg3_value)
        arg2_value, arg3_value = self.convert_nil(arg2_value, arg3_value)

        if arg2_type != TYPE_NIL and arg3_type != TYPE_NIL:
            if arg2_type != arg3_type:
                self.error_handler.error_exit(
                    53, "JUMPIFEQ has operands of different types"
                )

            if arg2_type == TYPE_INT:
                arg2_value = int(arg2_value)
                arg3_value = int(arg3_value)

            if arg2_type == TYPE_FLOAT:
                arg2_value = float(arg2_value)
                arg3_value = float(arg3_value)

        if arg2_value == arg3_value:
            jump = True

        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )
            
        if jump:
            self.inst_list.set_PC(inst_l.real_order)

    def interpret_jumpifneqs(self, inst):
        if DEBUG:
            print("Interpreting {}".format(inst.opcode))
        jump = False
        arg2_value, arg3_value, arg2_type, arg3_type = self.stack_get_operands()
        arg2_value, arg3_value = self.convert_bool(arg2_value, arg3_value)
        arg2_value, arg3_value = self.convert_nil(arg2_value, arg3_value)

        if arg2_type != TYPE_NIL and arg3_type != TYPE_NIL:
            if arg2_type != arg3_type:
                self.error_handler.error_exit(
                    53, "JUMPIFEQ has operands of different types"
                )

            if arg2_type == TYPE_INT:
                arg2_value = int(arg2_value)
                arg3_value = int(arg3_value)

            if arg2_type == TYPE_FLOAT:
                arg2_value = float(arg2_value)
                arg3_value = float(arg3_value)

        if arg2_value != arg3_value:
            jump = True

        try:
            inst_l = self.inst_list.labels[inst.arg1.text]
        except KeyError:
            self.inst_list.error_handler.error_exit(
                52, "Jump to undefined label {}".format(inst.arg1.text)
            )

        if jump:
            self.inst_list.set_PC(inst_l.real_order)

    def stack_get_operands(self):
        if len(self.data_stack) < 2:
            self.error_handler.error_exit(56, "Missing value on stack")
        symb2_value, symb2_type = self.data_stack.pop()
        symb_value, symb_type = self.data_stack.pop()
        return symb_value, symb2_value, symb_type, symb2_type

    def stack_arithmetic_check(self, inst):
        operand_1_value, operand_2_value, operand_1_type, operand_2_type = self.stack_get_operands()

        if operand_1_type != operand_2_type:
            self.error_handler.error_exit(
                53, "Arithmetic operation operands have different types"
            )
        if inst.opcode in ["ADDS", "MULS", "SUBS"]:
            if operand_1_type != TYPE_INT and operand_1_type != TYPE_FLOAT:
                self.error_handler.error_exit(
                    53,
                    "Arithmetic operations ADDS, MULS, SUBS support only INT or FLOAT operands",
                )
        elif inst.opcode == "DIVS" and operand_1_type != TYPE_FLOAT:
            self.error_handler.error_exit(
                53,
                "DIVS supports only float operands",
            )
        elif inst.opcode == "IDIV" and operand_1_type != TYPE_INT:
            self.error_handler.error_exit(
                53,
                "IDIVS supports only INT operands",
            )

        if inst.opcode in ["DIVS", "IDIVS"]:
            if int(operand_2_value) == 0:
                self.error_handler.error_exit(57, "Attempting zero devision")

        return operand_1_type, operand_1_value, operand_2_value


    def stack_relation_check(self, inst):
        operand_1_value, operand_2_value, operand_1_type, operand_2_type = self.stack_get_operands()

        if operand_1_type != TYPE_NIL and operand_2_type != TYPE_NIL:
            if operand_1_type != operand_2_type:
                self.error_handler.error_exit(
                    53, "Relation operation operands have different types"
                )
        if inst.opcode in ["LTS", "GTS"]:
            if operand_1_type not in [TYPE_INT, TYPE_BOOL, TYPE_STRING, TYPE_FLOAT] or operand_2_type not in [TYPE_INT, TYPE_BOOL, TYPE_STRING, TYPE_FLOAT]:
                self.error_handler.error_exit(
                    53,
                    "Relational operations LTS, GTS support only INT, STRING and BOOL operands",
                )
        elif inst.opcode == "EQS" and operand_1_type not in [
            TYPE_INT,
            TYPE_BOOL,
            TYPE_STRING,
            TYPE_NIL,
            TYPE_FLOAT,
        ]:

            self.error_handler.error_exit(
                53,
                "EQS supports only INT, STRING, BOOL and FLOAT operands",
            )

        r_value_1 = operand_1_value
        r_value_2 = operand_2_value

        if operand_1_type != TYPE_NIL and operand_2_type != TYPE_NIL:
            if operand_1_type == TYPE_INT:
                r_value_1 = int(operand_1_value)
                r_value_2 = int(operand_2_value)
            elif operand_1_type == TYPE_FLOAT:
                r_value_1 = float(operand_1_value)
                r_value_2 = float(operand_2_value)

        return r_value_1, r_value_2

    def stack_logical_check(self, inst):
        if inst.opcode != "NOTS":
            operand_1_value, operand_2_value, operand_1_type, operand_2_type = self.stack_get_operands()
        else:
            if len(self.data_stack) < 1:
                self.error_handler.error_exit(56, "Missing value on stack")
            operand_1_value, operand_1_type = self.data_stack.pop()
            operand_2_type = None
            operand_2_value = None

        if operand_1_type != TYPE_BOOL:
            self.error_handler.error_exit(53, "Logical operation operand is not bool")

        if operand_2_type is not None and operand_2_type != TYPE_BOOL:
            self.error_handler.error_exit(53, "Logical operation operand is not bool")

        return operand_1_value, operand_2_value





### Pomocne ###

    def get_var(self, var_name, with_value):
        frame, name = re.split("@", var_name)
        if frame == "GF":
            succ, var = self.frames.GF_get(name)
        if frame == "LF":
            succ, var = self.frames.LF_get(name)
        if frame == "TF":
            succ, var = self.frames.TF_get(name)
        if succ == False:
            self.error_handler.error_exit(54, "Variable does not exist")
        if with_value and var.value is None:
            self.error_handler.error_exit(56, "Variable defined, but without value")
        return var

    def get_type(self, var_type):
        if var_type.lower() == "nil":
            return TYPE_NIL
        if var_type.lower() == "bool":
            return TYPE_BOOL
        if var_type.lower() == "int":
            return TYPE_INT
        if var_type.lower() == "string":
            return TYPE_STRING
        if var_type.lower() == "float":
            return TYPE_FLOAT

    def arithmetic_operation_check(self, inst):
        operand_1_value, operand_1_type = self.get_symbol(inst.arg2, True)
        operand_2_value, operand_2_type = self.get_symbol(inst.arg3, True)

        if operand_1_type != operand_2_type:
            self.error_handler.error_exit(
                53, "Arithmetic operation operands have different types"
            )
        if inst.opcode in ["ADD", "MUL", "SUB"]:
            if operand_1_type != TYPE_INT and operand_1_type != TYPE_FLOAT:
                self.error_handler.error_exit(
                    53,
                    "Arithmetic operations ADD, MUL, SUB support only INT or FLOAT operands",
                )
        elif inst.opcode == "DIV" and operand_1_type != TYPE_FLOAT:
            self.error_handler.error_exit(
                53,
                "DIV supports only float operands",
            )
        elif inst.opcode == "IDIV" and operand_1_type != TYPE_INT:
            self.error_handler.error_exit(
                53,
                "IDIV supports only INT operands",
            )

        if inst.opcode in ["DIV", "IDIV"]:
            if int(operand_2_value) == 0:
                self.error_handler.error_exit(57, "Attempting zero devision")

        return operand_1_type, operand_1_value, operand_2_value

    def relation_operation_check(self, inst):
        operand_1_value, operand_1_type = self.get_symbol(inst.arg2, True)
        operand_2_value, operand_2_type = self.get_symbol(inst.arg3, True)

        if operand_1_type != TYPE_NIL and operand_2_type != TYPE_NIL:
            if operand_1_type != operand_2_type:
                self.error_handler.error_exit(
                    53, "Relation operation operands have different types"
                )
        if inst.opcode in ["LT", "GT"]:
            if operand_1_type not in [TYPE_INT, TYPE_BOOL, TYPE_STRING, TYPE_FLOAT] or operand_2_type not in [TYPE_INT, TYPE_BOOL, TYPE_STRING, TYPE_FLOAT]:
                self.error_handler.error_exit(
                    53,
                    "Relational operations LT, GT support only INT, STRING and BOOL operands",
                )
        elif inst.opcode == "EQ" and operand_1_type not in [
            TYPE_INT,
            TYPE_BOOL,
            TYPE_STRING,
            TYPE_NIL,
            TYPE_FLOAT,
        ]:

            self.error_handler.error_exit(
                53,
                "EQ supports only INT, STRING, BOOL and FLOAT operands",
            )

        r_value_1 = operand_1_value
        r_value_2 = operand_2_value

        if operand_1_type != TYPE_NIL and operand_2_type != TYPE_NIL:
            if operand_1_type == TYPE_INT:
                r_value_1 = int(operand_1_value)
                r_value_2 = int(operand_2_value)
            elif operand_1_type == TYPE_FLOAT:
                r_value_1 = float(operand_1_value)
                r_value_2 = float(operand_2_value)

        return r_value_1, r_value_2

    def logical_operation_check(self, inst):
        operand_1_value, operand_1_type = self.get_symbol(inst.arg2, True)
        if inst.opcode != "NOT":
            operand_2_value, operand_2_type = self.get_symbol(inst.arg3, True)
        else:
            operand_2_type = None
            operand_2_value = None

        if operand_1_type != TYPE_BOOL:
            self.error_handler.error_exit(53, "Logical operation operand is not bool")

        if operand_2_type is not None and operand_2_type != TYPE_BOOL:
            self.error_handler.error_exit(53, "Logical operation operand is not bool")

        return operand_1_value, operand_2_value

    def convert_bool(self, value_1, value_2):
        if value_1 == "true":
            value_1 = True
        if value_1 == "false":
            value_1 = False
        if value_2 == "true":
            value_2 = True
        if value_2 == "false":
            value_2 = False
        return value_1, value_2

    def convert_nil(self, value_1, value_2):
        if value_1 == "nil":
            value_1 = None
        if value_2 == "nil":
            value_2 = None
        return value_1, value_2

    def get_symbol(self, arg, not_null):
        if arg.arg_type == "var":
            var = self.get_var(arg.text, False)
            if not_null:
                if var.value is None or var.type is None:
                    self.error_handler.error_exit(
                        56, "Variable is defined, but withou value"
                    )
            r_value = var.value
            r_type = var.type

        else:
            r_type = self.get_type(arg.arg_type)
            r_value = arg.text
        return r_value, r_type

    def pop_stack_operands(self):
        pass
