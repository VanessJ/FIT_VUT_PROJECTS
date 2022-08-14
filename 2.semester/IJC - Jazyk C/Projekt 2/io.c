// # hstruct.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2

#include "io.h"

int get_word(char *s, int max, FILE *f){

    if (f == NULL || s == NULL){
      return EOF;  
    }
        

    int c = 0; // int for EOF

    do {
        c = fgetc(f);
        if (c == EOF)
            return EOF;
    } while(isspace(c));

    if(c == EOF){
         return EOF;
    } 

    s[0] = c;
    int i = 1;

    while(i<max-1){
        c = fgetc(f);
        if((c == EOF)|| (isspace(c))) {
            break;
        }
        s[i] = c;
        i++;
    }
    s[i]='\0'; 
    
    if(i == max -1){ 
       while((c = fgetc(f)) != EOF){
           if(isspace(c)){

           break;
           }

           i++;
       }
    }
    return i;
}

