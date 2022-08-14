// # htab_lookup_add.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include "htab.h"
#include "hstruct.h"

htab_iterator_t htab_lookup_add(htab_t * t, htab_key_t key){
    
    size_t index = (htab_hash_fun(key) % t-> arr_size);
    htab_iterator_t it = iterator_set(t->arr[index], t, index);

    while (htab_iterator_valid(it) && it.idx == index) {
        if ((strcmp(htab_iterator_get_key(it), key)) == 0) {
            return it;
        }

        it = htab_iterator_next(it);
    }

    it.ptr = malloc(sizeof(struct htab_item));
    if (it.ptr == NULL) {
        fprintf(stderr, "Alokacia tabulky zlyhala\n");
        return htab_end(t);
    }

    it.ptr->key = malloc(strlen(key) + 1);

    if (it.ptr->key == NULL) {
        free(it.ptr);
        return htab_end(t);
    }
    
    strcpy(it.ptr->key, key);
    htab_iterator_set_value(it, 0);
    it.ptr->next = t->arr[index];
    t->size++;
    t->arr[index] = it.ptr;
    return it;
}