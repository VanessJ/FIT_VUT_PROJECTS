// # htab_free.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "htab.h"
#include "hstruct.h"

void htab_free(htab_t * t){
    htab_clear(t);
    free(t);

}