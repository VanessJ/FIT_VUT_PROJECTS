// # iterator_set.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "hstruct.h"

htab_iterator_t iterator_set(struct htab_item * ptr, const htab_t * t, size_t index){
    htab_iterator_t it;
    it.ptr = ptr;
    it.t = t;
    it.idx = index;
    return it;

}