// # error.h
// # Riešenie IJC-DU1 b), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1


#ifndef ERROR_H
#define ERROR_H

void warning_msg(const char *fmt, ...);
void error_exit(const char *fmt, ...);

#endif