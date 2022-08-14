"""
Brief:  IPP 2020/21 assigment - error-handling class
Author: Vanessa Jóriová, xjorio00
Date: 09.4.2021
"""
import sys


class ErrorHandler:
    """ Class responsible for exiting with correct exit code and proper exit messege """

    errors = {
        10: "chybějící parametr skriptu (je-li třeba) nebo použití zakázané kombinace parametrů",
        11: "Chyba při otevírání vstupních souborů (např. neexistence, nedostatečné oprávnění)",
        12: "Chyba při otevření výstupních souborů pro zápis (např. nedostatečné oprávnění)",
        31: "chybný XML formát ve vstupním souboru (soubor není tzv. dobře formátovaný, angl. well-formed",
        52: "chyba při sémantických kontrolách vstupního kódu v IPPcode21 (např. použití nedefinovaného návěští, redefinice proměnné)",
        53: "běhová chyba interpretace – špatné typy operandů",
        54: "běhová chyba interpretace – přístup k neexistující proměnné (rámec existuje)",
        55: "-běhová chyba interpretace – rámec neexistuje (např. čtení z prázdného zásobníku rámců)",
        56: "běhová chyba interpretace – chybějící hodnota (v proměnné, na datovém zásobníku nebo v zásobníku volání)",
        57: "běhová chyba interpretace – špatná hodnota operandu (např. dělení nulou, špatná návratová hodnota instrukce EXIT)",
        58: "běhová chyba interpretace – chybná práce s řetězcem.",
    }

    def __init__(self):
        pass

    def error_exit(self, err_nmbr, msg=None):
        """ exits with error code and custom/default message """
        if msg:
            print(msg, file=sys.stderr)
        else:
            print(self.errors[err_nmbr], file=sys.stderr)
        # print(err_nmbr)
        sys.exit(err_nmbr)
