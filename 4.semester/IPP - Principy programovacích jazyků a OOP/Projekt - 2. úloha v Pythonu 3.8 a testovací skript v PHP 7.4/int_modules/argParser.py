"""
Brief:  IPP 2020/21 assigment - class processing program arguments
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""
import argparse
import sys
from int_modules.errorHandler import ErrorHandler


class ArgParser:
    """ Class processing program arguments """

    def get_args(self):
        """ Gets command line arguments """

        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("--help", action="store_true", help=argparse.SUPPRESS)
        parser.add_argument("--source", action="store", type=str, dest="source")
        parser.add_argument("--input", action="store", type=str, dest="input")
        parser.add_argument("--stats", action="store", type=str, dest="stats")
        parser.add_argument("--insts", action="store_true")
        parser.add_argument("--hot", action="store_true")
        parser.add_argument("--vars", action="store_true")

        args = parser.parse_args()
        return args

    def get_and_chech_args(self):
        """ Returns parsed arguments """
        args = self.get_args()
        arg_src, arg_input, arg_stats = self.check_args(args)
        return arg_src, arg_input, arg_stats

    def check_args(self, args):
        """ Checks and handles incorrect arguments """

        arg_src = None
        arg_input = None
        arg_stats = None
        error_handler = ErrorHandler()
        if args.help:
            if len(sys.argv) != 2:
                error_handler.error_exit(
                    10, "Another arguments in combination with --help not supported"
                )
            print(
                "Interpret that loads xml representation of code and input values and interprets given program."
            )
            print(
                "Interpret needs one of the following arguments --source=source, --input=input. "
            )
            print("If only one argument is given, the other is loaded from stdin.")
            print("For more info and info on extensions arguments check:")
            print(
                "https://wis.fit.vutbr.cz/FIT/st/cfs.php.cs?file=%2Fcourse%2FIPP-IT%2Fprojects%2F2020-2021%2FZadani%2Fipp21spec.pdf&cid=14009 "
            )
            sys.exit(0)
        if args.source:
            arg_src = args.source
        if args.input:
            arg_input = args.input
        if args.stats:
            arg_stats = args.stats
        if not args.input and not args.source:
            error_handler.error_exit(
                10,
                "Program requires at least one of following arguments: --source, --input",
            )
        if (args.vars or args.hot or args.insts) and not args.stats:
            error_handler.error_exit(10, "--Stats argument not present")
        return arg_src, arg_input, arg_stats
