// # bitset.h
// # Riešenie IJC-DU1 a), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1
// # Popis: makrá a funkcie pre prácu s bitovým polom 


#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <assert.h>

#include "error.h"


#ifndef BITSET_H
#define BITSET_H

typedef unsigned long bitset_t[];
typedef unsigned long bitset_index_t;


#define SIZE (sizeof(unsigned long) * CHAR_BIT)


#define NUM_OF_UL(velikost) (velikost / SIZE) + (velikost % SIZE == 0 ? 1 : 2)



#define SETBIT(jmeno_pole, index, vyraz) \
        (vyraz) ? (jmeno_pole[(index)/SIZE] |=  (1UL << ((index)%SIZE))) :   \
                     (jmeno_pole[(index)/SIZE] &= ~(1UL << ((index)%SIZE))) 



#define GETBIT(jmeno_pole, index) ((jmeno_pole[((index)/SIZE)] & (1UL << ((index)%SIZE))) != 0)



#define bitset_create(jmeno_pole, velikost)_Static_assert((velikost > 1  ), "Velkost pola nesmie byt mensia ako 2.\n"); \
                                          unsigned long jmeno_pole[NUM_OF_UL(velikost)] = {velikost, 0}


#define bitset_alloc(jmeno_pole, velikost) \
    assert(velikost > 1 && "Velkost pola nesmie byt mensia ako 2.\n"); \
    unsigned long * jmeno_pole = calloc(NUM_OF_UL(velikost), sizeof(unsigned long)); \
    if (jmeno_pole == NULL ) { \
        error_exit("Chyba pri alokacii pola\n"); \
    } \
    *jmeno_pole = velikost;

    

#define bitset_free(jmeno_pole) \
    free(jmeno_pole)



#ifndef USE_INLINE

    
    #define bitset_size(jmeno_pole) \
        jmeno_pole[0]


    #define bitset_setbit(jmeno_pole, index, vyraz)                                                                          \
        if ((unsigned long)index >= bitset_size(jmeno_pole)) {  \
            error_exit("bitset_setbit: Index %lu mimo rozsah 0..%lu", (unsigned long)index, (unsigned long)(jmeno_pole[0]-1)); \
        }\
        (vyraz) ? (jmeno_pole[((unsigned long)index)/SIZE + 1] |=  (1UL << (((unsigned long)index)%SIZE))) :   \
                  (jmeno_pole[((unsigned long)index)/SIZE + 1] &= ~(1UL << (((unsigned long)index)%SIZE))) 

    


    #define bitset_getbit(jmeno_pole, index)                                                                                              \
        ((unsigned long)index >= bitset_size(jmeno_pole)) ?                                                                                 \
        (error_exit("bitset_getbit: Index %lu mimo rozsah 0..%lu", (unsigned long)index, (unsigned long)(jmeno_pole[0]-1)), -1) :         \
        ((jmeno_pole[(((unsigned long)index)/SIZE) + 1] & (1UL << (((unsigned long)index)%SIZE))) ? 1 : 0)


#else 

    inline unsigned long bitset_size(bitset_t jmeno_pole) {
        return jmeno_pole[0];
    }

    inline void bitset_setbit(bitset_t jmeno_pole, bitset_index_t index, int vyraz) {

       if (index >= bitset_size(jmeno_pole)){
        error_exit("bitset_setbit: Index %lu mimo rozsah 0..%lu", index, (bitset_size(jmeno_pole)-1));
        } 
        if (vyraz) {
            jmeno_pole[(index)/SIZE + 1] |=  (1UL << ((index)%SIZE));
        }
        else {
            (jmeno_pole[(index)/SIZE + 1] &= ~(1UL << ((index)%SIZE)));
         }


    }

    inline unsigned long bitset_getbit(bitset_t jmeno_pole, bitset_index_t index) {

        if (index >= bitset_size(jmeno_pole)){
        error_exit("bitset_getbit: Index %lu mimo rozsah 0..%lu", index, (bitset_size(jmeno_pole)-1));
        } 
        if (jmeno_pole[index / SIZE + 1 ] & (1UL << ((index)%SIZE))) {
            return 1;
            }
            else return 0;

    }

    #endif

    #endif







    