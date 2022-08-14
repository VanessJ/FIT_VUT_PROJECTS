// # htab_erase.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"


void htab_erase(htab_t * t, htab_iterator_t it){
    htab_iterator_t prev;
    htab_iterator_t i = htab_begin(t);

    while(htab_iterator_valid(i)){
        if (htab_iterator_equal(i, it)){
            break;
        }
        prev = i;
        i = htab_iterator_next(i);
    }

    if (htab_iterator_valid(prev) && it.ptr->next != NULL){
        prev.ptr->next = it.ptr->next;
    }
     if(it.ptr->key != NULL){
         free((char *)it.ptr->key);
     }
     if(it.ptr != NULL){
         free(it.ptr);
     }
}