// # eratostenes.c
// # Riešenie IJC-DU1 a), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1
// # Popis: Eratostenovo sito pre výpočet prvočísel 

#include <stdio.h>
#include <math.h>
#include "bitset.h"


void Eratosthenes(bitset_t pole) {
    unsigned long size = pole[0];
    unsigned long limit = sqrt(bitset_size(pole));
    bitset_setbit(pole, 0, 1);
    bitset_setbit(pole, 1, 1);

    for (bitset_index_t i = 2; i <= limit; i++) {
        if ((bitset_getbit(pole,i) == 0)) {
            for(bitset_index_t j = 2 * i; j < size; j+=i) {
                bitset_setbit(pole, j, 1);
            }
        }
    }
}