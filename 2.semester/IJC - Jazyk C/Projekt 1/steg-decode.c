// # steg-decode.c
// # Riešenie IJC-DU1 b), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1
// # Popis: rozšifruje správu zakódovanú v ppm obrázku


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#include "eratosthenes.h"
#include "error.h"
#include "ppm.h"
#include "bitset.h"

int main(int argc, char *argv[]) {
	if (argc != 2) {
		error_exit("Nespravne argumenty programu.\n");
        }   
	
	struct ppm* image = ppm_read(argv[1]);
    if (image == NULL) {
			error_exit("Nespravny format PPM suboru.\n");
		}
    char *data = image->data;
    unsigned long size = (3 * image->xsize * image->ysize);
    char message[] = {0};
    int bit_counter =0;

    bitset_alloc(primes, size);
    Eratosthenes(primes);
   

     for (unsigned long i = 23; i <= size; i++){
         if (bitset_getbit(primes, i) == 0) {
			SETBIT(message, bit_counter, GETBIT((&(data[i+1])), 0));
            bit_counter++;
    
        }
        if (bit_counter == 8){
            if(message[0] == '\0'){
                putchar('\n');
                bitset_free(primes);
                ppm_free(image);
                return EXIT_SUCCESS;
            }
        putchar(message[0]);
        bit_counter = 0;
        *message = 0;
        }

     }

    bitset_free(primes);
    ppm_free(image);
    error_exit("Nespravne ukoncena sprava\n");	

	return EXIT_FAILURE;
}



