##
# @file gui_calculator.py
# @brief GUI for our calculator
# @author Magdaléna Bellayová, Tomáš Mikeska
# @date April 2020
#

import os
import sys
from tkinter import Tk, Button, Label, Entry, PhotoImage, END, FLAT, W, E, RIGHT
import math_lib
from colors import Colors


##
# @brief Calculator main window GUI
#
class CalculatorGUI:
    answer = 0
    font_name = 'Consolas 16'
    newtext = ''

    ##
    # @brief Function for initialization of displayed window and self.create_grid_btns.
    # @param root window
    #
    def __init__(self, root):
        self.root = root
        root.title('(Almost) Calculator Lite')
        self.setup_appicon(root)
        self.setup_layout()
        self.add_help_button()
        self.add_button_grid()

    def setup_appicon(self, tk_instance):
        if 'nt' == os.name:
            tk_instance.iconbitmap(os.path.join(os.path.dirname(__file__), 'calc.ico'))
        else:
            rootdir = (sys._MEIPASS + '/files/') if hasattr(sys, '_MEIPASS') else os.path.dirname(__file__)
            tk_instance.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file=os.path.join(rootdir, 'calc.png')))

    def setup_layout(self):
        root.geometry()
        root.resizable(0, 0)
        self.equation_input = Entry(root,
                                    fg='white',
                                    relief=FLAT,
                                    state='readonly',
                                    readonlybackground=Colors.dark_bg,
                                    bg=Colors.dark_bg,
                                    font='Consolas 21',
                                    highlightcolor=Colors.dark_bg,
                                    highlightbackground=Colors.dark_bg,
                                    borderwidth=0,
                                    highlightthickness=1,
                                    bd=0)
        self.equation_input.grid(row=0, column=0, columnspan=6, sticky=W + E)
        self.equation_input.focus_set()  # Sets focus on the input text area
        self.result_input = Entry(root,
                                  fg='white',
                                  relief=FLAT,
                                  state='readonly',
                                  readonlybackground=Colors.dark_bg,
                                  bg=Colors.dark_bg,
                                  font='Consolas 32',
                                  borderwidth=0,
                                  highlightthickness=0,
                                  bd=0,
                                  justify=RIGHT)
        self.result_input.grid(row=1, column=0, columnspan=6, sticky=W + E)

    def add_help_button(self):
        Button(text='?',
               width=6,
               height=1,
               fg=Colors.text_light,
               bg=Colors.dark_bg,
               relief=FLAT,
               font='Consolas 10',
               borderwidth=0,
               highlightthickness=0,
               bd=0,
               command=lambda: self.help()).grid(row=0, column=5)

    def add_button_grid(self):
        self.create_grid_btn('=', self.equals, bg=Colors.dark_bg, fg=Colors.text_light).grid(row=5, column=0)

        self.create_grid_btn('AC', self.clearall, bg=Colors.accent_darker).grid(row=2, column=5)

        self.create_grid_btn('C', self.backspace, bg=Colors.accent_darker).grid(row=2, column=4)

        self.create_grid_btn('+', lambda: self.action(' + ')).grid(row=4, column=3)

        self.create_grid_btn('×', lambda: self.action(' x ')).grid(row=2, column=3)

        self.create_grid_btn('-', lambda: self.action(' - ')).grid(row=5, column=3)

        self.create_grid_btn('7', lambda: self.action('7')).grid(row=2, column=0)

        self.create_grid_btn('8', lambda: self.action('8')).grid(row=2, column=1)

        self.create_grid_btn('9', lambda: self.action('9')).grid(row=2, column=2)

        self.create_grid_btn('4', lambda: self.action('4')).grid(row=3, column=0)

        self.create_grid_btn('5', lambda: self.action('5')).grid(row=3, column=1)

        self.create_grid_btn('6', lambda: self.action('6')).grid(row=3, column=2)

        self.create_grid_btn('1', lambda: self.action('1')).grid(row=4, column=0)

        self.create_grid_btn('2', lambda: self.action('2')).grid(row=4, column=1)

        self.create_grid_btn('3', lambda: self.action('3')).grid(row=4, column=2)

        self.create_grid_btn('0', lambda: self.action('0')).grid(row=5, column=1)

        self.create_grid_btn('.', lambda: self.action('.')).grid(row=5, column=2)

        self.create_grid_btn('/', lambda: self.action(' / '),).grid(row=3, column=3)

        self.create_grid_btn('!', lambda: self.action(' ! '), bg=Colors.accent).grid(row=4, column=4)

        self.create_grid_btn('sin', lambda: self.action(' sin '), bg=Colors.accent).grid(row=5, column=4)

        self.create_grid_btn('cos', lambda: self.action(' cos '), bg=Colors.accent).grid(row=5, column=5)

        self.create_grid_btn('neg', lambda: self.action(' neg '), bg=Colors.accent).grid(row=4, column=5)

        self.create_grid_btn('\u221a', lambda: self.action(' \u221a '), bg=Colors.accent).grid(row=3, column=5)

        self.create_grid_btn('^', lambda: self.action(' ^ '), bg=Colors.accent).grid(row=3, column=4)

    ##
    # @brief Create predefined calculator grid button
    # @param text Button text
    # @param command Callback on click
    # @param bg Background color
    # @param fg Text color
    #
    def create_grid_btn(self, text, command, bg=Colors.light_bg, fg=Colors.text_dark):
        return Button(self.root,
                      text=text,
                      width=7,
                      height=3,
                      fg=fg,
                      bg=bg,
                      relief=FLAT,
                      borderwidth=0,
                      highlightthickness=0,
                      bd=0,
                      font=self.font_name,
                      command=command)

    ##
    # @brief Function that splits the string into the list.
    #
    def splitandreplace(self):
        self.newtext = self.newtext.replace('x', '*')
        self.texttosplit = ' '.join(self.newtext.split())
        self.spltexpr = self.texttosplit.split()

    ##
    # @brief Action for pressing equals on calculator,result is displayed on calculator
    #
    def equals(self):
        self.splitandreplace()
        try:
            for i in range(0, len(self.spltexpr)):
                if self.spltexpr[i] == 'neg':
                    self.spltexpr[i + 1] = str(math_lib.neg(float(self.spltexpr[i + 1])))
                    for j in range(i, 0, -1):
                        self.spltexpr[j] = self.spltexpr[j - 1]
                    self.spltexpr[0] = ''
            for i in range(0, len(self.spltexpr)):
                if self.spltexpr[i] == 'sin':
                    self.spltexpr[i + 1] = str(math_lib.sinus(float(self.spltexpr[i + 1])))
                    for j in range(i, 0, -1):
                        self.spltexpr[j] = self.spltexpr[j - 1]
                    self.spltexpr[0] = ''
                if self.spltexpr[i] == 'cos':
                    self.spltexpr[i + 1] = str(math_lib.cosine(float(self.spltexpr[i + 1])))
                    for j in range(i, 0, -1):
                        self.spltexpr[j] = self.spltexpr[j - 1]
                    self.spltexpr[0] = ''
                if self.spltexpr[i] == '!':
                    self.spltexpr[i] = str(math_lib.factorial(float(self.spltexpr[i - 1])))
                    for j in range(i - 1, 0, -1):
                        self.spltexpr[j] = self.spltexpr[j - 1]
                    self.spltexpr[0] = ''
            for i in range(0, len(self.spltexpr)):
                if self.spltexpr[i] == '^':
                    self.spltexpr[i + 1] = str(math_lib.pow(float(self.spltexpr[i - 1]), int(self.spltexpr[i + 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
                if self.spltexpr[i] == '\u221a':
                    self.spltexpr[i + 1] = str(math_lib.root(float(self.spltexpr[i + 1]),int(self.spltexpr[i - 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
                if self.spltexpr[i] == '*':
                    self.spltexpr[i + 1] = str(math_lib.mul(
                        float(self.spltexpr[i - 1]), float(self.spltexpr[i + 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
                if self.spltexpr[i] == '/':
                    self.spltexpr[i + 1] = str(math_lib.div(
                        float(self.spltexpr[i - 1]), float(self.spltexpr[i + 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
            for i in range(0, len(self.spltexpr)):
                if self.spltexpr[i] == '+':
                    self.spltexpr[i + 1] = str(math_lib.add(
                        float(self.spltexpr[i - 1]), float(self.spltexpr[i + 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
                if self.spltexpr[i] == '-':
                    self.spltexpr[i + 1] = str(math_lib.sub(
                        float(self.spltexpr[i - 1]), float(self.spltexpr[i + 1])))
                    for j in range(i, 1, -1):
                        self.spltexpr[j] = self.spltexpr[j - 2]
                    self.spltexpr[0] = ''
                    self.spltexpr[1] = ''
            self.finaltext = ''.join(self.spltexpr)
            self.answer = float(self.finaltext)
        except ValueError:
            self.result_input.config(state='normal')
            self.result_input.delete(0, END)
            self.result_input.insert(0, 'Invalid Input!')
            self.result_input.config(state='readonly')
        except SyntaxError or NameError:
            self.result_input.config(state='normal')
            self.result_input.delete(0, END)
            self.result_input.insert(0, 'Invalid Input!')
            self.result_input.config(state='readonly')
        else:
            self.result_input.config(state='normal')
            self.result_input.delete(0, END)
            self.result_input.insert(0, self.finaltext)
            self.result_input.config(state='readonly')

    ##
    # @brief Action for pressing AC on calculator, display is cleared
    #
    def clearall(self):
        '''when clear self.create_grid_btn is pressed,clears the text input area'''
        self.equation_input.config(state='normal')
        self.result_input.config(state='normal')
        self.result_input.delete(0, END)
        self.equation_input.delete(0, END)
        self.newtext = ''
        self.equation_input.config(state='readonly')
        self.result_input.config(state='readonly')

    ##
    # @brief Action for pressing C on calculator, one character from display is deleted
    #
    def backspace(self):
        self.equation_input.config(state='normal')
        self.txt = self.equation_input.get()[:-1]
        self.equation_input.delete(0, END)
        self.equation_input.insert(0, self.txt)
        self.newtext = self.newtext[:-1]
        self.equation_input.config(state='readonly')

    ##
    # @brief Action for pressing other self.create_grid_btns on calculator, display is cleared
    # @param argi text of the self.create_grid_btn.
    #
    def action(self, button_text):
        '''pressed self.create_grid_btn's value is inserted into the end of the text area'''
        self.equation_input.config(state='normal')
        self.newtext += button_text
        self.equation_input.insert(END, button_text)
        self.equation_input.config(state='readonly')

    ##
    # @brief Function for displaying help for user
    #
    def help(self):
        help_root = Tk()
        help_root.title('Help')
        self.setup_appicon(help_root)
        help_root.geometry()
        help_root.resizable(0, 0)
        help_label2 = Label(
            help_root, text='AC - delete all', font='Consolas 10')
        help_label2.pack()
        help_label3 = Label(
            help_root, text='C - delete one character', font='Consolas 10')
        help_label3.pack()
        help_label4 = Label(
            help_root, text='\u221a - root of number after, number before determines which root', font='Consolas 10')
        help_label4.pack()
        help_label5 = Label(
            help_root, text='^ - power of number before, number after determines which power ', font='Consolas 10')
        help_label5.pack()
        help_label6 = Label(
            help_root, text='! - factorial of number before ', font='Consolas 10')
        help_label6.pack()
        help_label7 = Label(
            help_root, text='neg - returns netive number after', font='Consolas 10')
        help_label7.pack()
        help_label7 = Label(
            help_root, text='sin, cos - sinus/cosine of number after', font='Consolas 10')
        help_label7.pack()
        help_label8 = Label(
            help_root, text='+, -, x, / - plus/minus/multiplication/division', font='Consolas 10')
        help_label8.pack()
        help_label9 = Label(
            help_root, text='= - writes the result ', font='Consolas 10')
        help_label9.pack()
        help_root.mainloop()


# Creating window and object in that window.
root = Tk()
obj = CalculatorGUI(root)
root.mainloop()
