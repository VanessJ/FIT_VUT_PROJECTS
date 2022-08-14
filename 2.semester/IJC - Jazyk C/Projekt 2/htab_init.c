// # htab_init.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

htab_t *htab_init(size_t n){
htab_t * t = malloc(sizeof(htab_t) + n * sizeof(struct htab_item *)); 
    if (t == NULL) {
        fprintf(stderr, "Error: alokacia pamate zlyhala\n");
        return NULL;
    }
    t->size = 0;;
    t->arr_size = n;
    for(size_t i = 0; i< n; i++ ){
        t->arr[i] = NULL;
    }
    return t;
}