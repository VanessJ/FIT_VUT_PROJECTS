// # hstruct.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2



#ifndef __HSTRUCT_H__
#define __HSTRUCT_H__

#include "htab.h"

typedef struct htab_item {
    htab_key_t key;
    htab_value_t value;
    struct htab_item * next;
} htab_item;


typedef struct htab {
    size_t size;
    size_t arr_size;
    struct htab_item *arr [];

} htab;


htab_iterator_t iterator_set(struct htab_item * ptr, const htab_t * t, size_t index);



#endif