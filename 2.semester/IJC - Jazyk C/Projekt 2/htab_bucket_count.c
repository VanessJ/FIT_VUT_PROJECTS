// # htab_bucket_count.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

size_t htab_bucket_count(const htab_t * t){
    if (t == NULL){
        return 0;
    }
    return t->arr_size;
}