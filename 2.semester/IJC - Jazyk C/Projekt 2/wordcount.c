// # wordcount.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include <stdio.h>
#include <stdlib.h>

#include "io.h"
#include "htab.h"

#define WORD_LIMIT 128

// pri vybere vhodnej velkosti som hladala predovsetkym prvocislo pre ulahcenie prace s tabulkou
// s vyberom vhodneho prvocisla mi pomohla aj stranka https://planetmath.org/goodhashtableprimes
// vybrana velkost umoznuje zaznamenat vsetky unikatne hesla v priemernej knihe
#define ARRAY_SIZE 12289

int main(void){

    char *s = malloc(WORD_LIMIT);
    if (s == NULL){
       fprintf(stderr, "Allokacia zlyhala\n");
       return 1; 
    }
    int length = 0;

    int warning_printed = 0;

    htab_t *table = htab_init(ARRAY_SIZE);
    if (table == NULL){
        fprintf(stderr, "Alokacia zlyhala\n");
    }

    while((length = get_word(s, WORD_LIMIT, stdin) != EOF)){
        if (length >= WORD_LIMIT && warning_printed == 0){
            fprintf(stderr, "Slovo prekrocilo limit\n");
            warning_printed++;
        }

        htab_iterator_t it = htab_lookup_add(table, s);
        if(htab_iterator_valid(it) == false){
            fprintf(stderr, "Error\n");
            free(s);
            htab_free(table);
            return 1;
        }

        htab_iterator_set_value(it, htab_iterator_get_value(it)+1);


    }

    for(htab_iterator_t i = htab_begin(table); htab_iterator_valid(i); i = htab_iterator_next(i)){

         printf("%s\t%d\n", htab_iterator_get_key(i), htab_iterator_get_value(i));
    }

    htab_free(table);
    free(s);
    return 0;

}
