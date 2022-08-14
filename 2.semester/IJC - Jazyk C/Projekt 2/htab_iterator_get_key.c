// # htab_iterator_get_key.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

htab_key_t htab_iterator_get_key(htab_iterator_t it){
    return it.ptr->key;
}