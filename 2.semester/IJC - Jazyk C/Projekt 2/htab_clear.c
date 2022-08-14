// # htab_clear.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "htab.h"
#include "hstruct.h"

void htab_clear(htab_t * t){

struct htab_item * temp;

    for(size_t i = 0; i < t->arr_size; i++){

        while (t->arr[i] != NULL){
            temp = t->arr[i]->next;
            free((char*)t->arr[i]->key);
            free(t->arr[i]);
            t->arr[i] = temp;
        }

    }
    t->size = 0;

}