// # error.c
// # Riešenie IJC-DU1 b), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1
// # Popis: modul pre výpis varovaní a errorov 


#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

#include "error.h"


void warning_msg(const char * fmt, ...) {
    va_list argPtr;
    va_start(argPtr, fmt);
    fprintf(stderr, "CHYBA: ");
    vfprintf(stderr, fmt, argPtr);
    fprintf(stderr, "\n");
    va_end(argPtr);
}


 void error_exit(const char *fmt, ...) {
    va_list argPtr;
    va_start(argPtr, fmt);
    fprintf(stderr, "Chyba: ");
    vfprintf(stderr, fmt, argPtr);
    fprintf(stderr, "\n");
    va_end(argPtr);
    exit(1);
}
