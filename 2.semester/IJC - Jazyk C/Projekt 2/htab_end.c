// # htab_end.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

htab_iterator_t htab_end(const htab_t * t){
    
    return iterator_set(NULL, t, t->arr_size); 
}