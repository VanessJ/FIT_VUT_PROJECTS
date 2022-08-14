"""
Brief:  IPP 2020/21 assigment - class handling frames of the program
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
Details:    IPPCode21 consists of various frames in which are variables stored:
            Global Frame (GF) is avalaible is always available, starts empty and 
            is filled with global variable.
            
            Local Frame (LF) is the current top of frame stack and starts undefined.
            Stores local variables and can be popped from top of the stack.
            
            Temporaly (TF) starts undefined and can be converted to Local Frame.  
"""


from int_modules.variable import Variable
from int_modules.errorHandler import ErrorHandler


class Frames:
    """ Class representing IPPCode21 memory model """

    def __init__(self):
        self.local_frame = None
        self.temp_frame = None
        self.global_frame = []
        self.frame_stack = []
        self.error_handler = ErrorHandler()

    def add_to_GF(self, variable):
        """
        Checks if variable is already defined in global frame - if not, variable is added
        """
        temp, succes = self.GF_get(variable.name)
        if not succes:
            self.global_frame.append(variable)
        else:
            self.error_handler.error_exit(
                52, "Variable already defined in global frame"
            )

    def add_to_LF(self, variable):
        """
        Checks if variable is already defined in local frame - if not, variable is added
        """
        if self.local_frame is None:
            self.error_handler.error_exit(55, "Local frame does not exist")
        temp, succes = self.LF_get(variable.name)
        if not succes:
            self.local_frame.append(variable)
        else:
            self.error_handler.error_exit(52, "Variable already defined in local frame")

    def add_to_TF(self, variable):
        """
        Checks if variable is already defined in temporaly frame - if not, variable is added
        """
        if self.temp_frame is None:
            self.error_handler.error_exit(55, "Temp frame does not exist")
        temp, succes = self.TF_get(variable.name)
        if not succes:
            self.temp_frame.append(variable)
        else:
            self.error_handler.error_exit(
                52, "Variable already defined in temporaly frame"
            )

    def GF_get(self, name):
        """
        Returns true and variable if variable present on global frame - returns false if not
        """
        for var in self.global_frame:
            if var.name == name:
                return True, var
        return False, None

    def LF_get(self, name):
        """
        Returns true and variable if variable present on local frame - returns false if not
        """
        if self.local_frame is None:
            self.error_handler.error_exit(55, "Local frame does not exist")
        for var in self.local_frame:
            if var.name == name:
                return True, var
        return False, None

    def TF_get(self, name):
        """
        Returns true and variable if variable present on temporaly frame - returns false if not
        """
        if self.temp_frame is None:
            self.error_handler.error_exit(55, "Temporary frame does not exist")
        for var in self.temp_frame:
            if var.name == name:
                return True, var
        return False, None

    def push_frame(self):
        """
        Converts temporaly frame into local frame and pushes local frame to the top of local frames stack
        """
        if self.temp_frame is None:
            self.error_handler.error_exit(55, "Temporary frame does not exist")
        self.frame_stack.append(self.temp_frame)
        self.local_frame = self.frame_stack[-1]
        self.temp_frame = None

    def pop_frame(self):
        """
        Pops local frame from the top of the local frame stack and converts it into temporaly frame
        """
        if len(self.frame_stack) < 1:
            self.error_handler.error_exit(55, "Frame stack is empty")
        self.temp_frame = self.frame_stack.pop()
        try:
            self.local_frame = self.frame_stack[-1]
        except IndexError:
            self.local_frame = None
