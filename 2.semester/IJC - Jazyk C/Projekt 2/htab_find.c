// # htab_find.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

htab_iterator_t htab_find(htab_t * t, htab_key_t key){
    size_t index = (htab_hash_fun(key) % t-> arr_size);
    htab_iterator_t it = iterator_set(t->arr[index], t, index);

        while (htab_iterator_valid(it) && it.idx == index) {
        if ((strcmp(htab_iterator_get_key(it), key)) == 0) {
            return it;
        }

        it = htab_iterator_next(it);
    }

     return htab_end(t);
}