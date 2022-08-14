// # htab_begin.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "htab.h"
#include "hstruct.h"

htab_iterator_t htab_begin(const htab_t * t){

    if (t == NULL){
        return iterator_set(NULL, NULL, 0);
    }


    for (size_t i = 0; i < t-> arr_size; i++){
        if(t->arr[i] != NULL){
            return iterator_set(t->arr[i], t, i);
        }
    }
    return iterator_set(NULL, t, 0);
}