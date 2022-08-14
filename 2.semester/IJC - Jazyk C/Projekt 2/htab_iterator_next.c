// # htab_iterator_next.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "htab.h"
#include "hstruct.h"


htab_iterator_t htab_iterator_next(htab_iterator_t it){
if (it.ptr->next == NULL) {

        
        if ((size_t)it.idx < it.t->arr_size - 1)

            for (size_t i = it.idx + 1; i < it.t->arr_size; i++) {
                if ((it.ptr = it.t->arr[i]) != NULL) {
                    it.idx = i;
                    return it;
                }
            }

        it = htab_end(it.t);
        return it;

    } 
        it.ptr = it.ptr->next;
    
    
    return it;
}