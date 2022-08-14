// # primes.c
// # Riešenie IJC-DU1, 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1 a)
// # Popis: s využitím Eratostenovho sita vypíše posledných 10 prvočísiel vzostupne 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "bitset.h"
#include "eratosthenes.h"


clock_t start;

#define LIMIT 500000000
#define PRIMES_COUNT 10

int main (void){

    start = clock();

    bitset_create(array,LIMIT);
    unsigned long primes[PRIMES_COUNT] = {0};
    int counter = 0;
    Eratosthenes(array);

    
    for(bitset_index_t i = LIMIT-1; i > 0; i--) {
        if (bitset_getbit(array,i) == 0) {
            primes[counter] = i;
            counter++;
            if (counter >= PRIMES_COUNT) {
                break;
           }
        }
            
    }
    


    for (int i = counter-1; i >= 0; i--) {
		printf("%lu\n", primes[i]);
	}

     fprintf(stderr, "Time=%.3g\n", (double)(clock()-start)/CLOCKS_PER_SEC); 

	return 0;


}
