// # bitset.c
// # Riešenie IJC-DU1 a), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1


#include <stdio.h>
#include <stdlib.h>

#include "bitset.h"

#ifdef USE_INLINE

extern inline unsigned long bitset_size(bitset_t jmeno_pole);
extern inline unsigned long bitset_getbit (bitset_t jmeno_pole, bitset_index_t index);
extern inline void bitset_setbit(bitset_t jmeno_pole, bitset_index_t index, int vyraz);    

#endif


