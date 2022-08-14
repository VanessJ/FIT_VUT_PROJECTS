// # tail.c
// # Riešenie IJC-DU2, 15.4.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preloženie: gcc 7.4.0
// # Zostavenie: IJC-DU2


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define DEFAULT_TAIL 10 
#define MAX_LENGTH 1023


#define NORMAL 0
#define PLUS_MODE 2 


int nmbr_parse(char * nmbr){
    char *buffer = NULL;
    int number = strtol(nmbr, &buffer, 10);
    if(!*buffer){
        if (number < 0 ){
            number*=-1;
        }
        return number;
    }
    else {
        return -1;
    }
}

void file_close(FILE *f){
    if (fclose(f) == EOF){
        fprintf(stderr, "Error closing file\n");
        exit(1);
    }
}




FILE * fileopen(char * filename){
    FILE * f;
    if (filename == NULL){
        f = stdin;
    } 
    else {
        f = fopen(filename, "r");
        if(f==NULL) {
            fprintf(stderr, "Subor sa neda otvorit!\n");
            exit(1);
        }
    }
    return f;
}

void tail_2 (FILE * f, int print_from_line){
    int c;
    char string[MAX_LENGTH+1];
    int index = 0;
    while (fgets(string, MAX_LENGTH, f) != NULL) {
       if (string[strlen(string) - 1] != '\n') {
            string[strlen(string)] = '\n';
            string[strlen(string) + 1] = '\0';

            do { 
                c = fgetc(f);
            }
            while (c != '\n');
        }
        

        index++;
        if (index >= print_from_line) {
            printf("%s", string);
           
        }
        
      
    }    

    
}

void tail(FILE * f, char * buffer[], int lines){
    char c;
    char string[MAX_LENGTH + 2];

    int i = 0;
    
    while(fgets(string, MAX_LENGTH + 1, f) != NULL){
        if (string[strlen(string) - 1] != '\n') {
            string[strlen(string)] = '\n';
            string[strlen(string) + 1] = '\0';
            do { 
                c = fgetc(f);
            }
            while (c != '\n');
        }

        strcpy(buffer[i % lines], string);
        i++;

    }

    if (lines > i) {
        lines = i;
    }

    int pos = i %lines;
    
    for(int j = pos; j < lines; j++){
        printf("%s", buffer[j]);
    }

    for(int j = 0; j < pos; j++){
        printf("%s", buffer[j]);
    }
    
}



void free_buffer(char ** buffer, int lines){
    for (int i = 0; i < lines; i++) {
        free(buffer[i]);
    }
    
    free(buffer);
}


char ** aloc_buffer(int lines){
    char ** buffer;
    buffer = malloc(lines * sizeof(char *));
    if (buffer == NULL) {
        return NULL;
    }
    for (int i = 0; i <lines; i++){
        buffer[i] = malloc((MAX_LENGTH + 2) * sizeof(char *));
        if (buffer[i] == NULL){
            free_buffer(buffer, i);
            return NULL;
        }

    }

    return buffer;
}




int main(int argc, char *argv[]){

    FILE * f;
    int parsed_nmbr = 0;
    int mode = NORMAL;
    

    switch(argc) {
        case 1: {
            f=fileopen(NULL);
            char ** buffer = aloc_buffer(DEFAULT_TAIL);
            if (buffer != NULL) {
                tail(f, buffer, DEFAULT_TAIL);
                free_buffer(buffer, DEFAULT_TAIL);
            }
            else{
                fprintf(stderr, "Alokacia zlyhala\n");
            }
            break;
        }
        case 2: {
            f = fileopen(argv[1]);
            char ** buffer = aloc_buffer(DEFAULT_TAIL);
            if (buffer != NULL) {
                tail(f, buffer, DEFAULT_TAIL);
                free_buffer(buffer, DEFAULT_TAIL);
            }
            else{
                fprintf(stderr, "Alokacia zlyhala\n");
            }

            break;
        }
        case 3: {
            if(strcmp(argv[1], "-n") != 0) {
                fprintf(stderr, "Zly argument programu!\n");
                return -1;
            }
            char arg_number[63];
            strncpy(arg_number, argv[2], 64);
            if (arg_number[0] == '+') {
                mode = PLUS_MODE;
                arg_number[0]='0'; 
            }
            parsed_nmbr = nmbr_parse(arg_number);
            if (parsed_nmbr == -1) {
                fprintf(stderr, "Zle zadany pocet riadkov\n");
                return -1;
            }

            f = fileopen(NULL);

            if (mode == PLUS_MODE){
                tail_2(f, parsed_nmbr);
            }
            else {
               char ** buffer = aloc_buffer(parsed_nmbr);
                if (buffer != NULL) {
                    tail(f, buffer, parsed_nmbr);
                    free_buffer(buffer, parsed_nmbr);
                }
                else{
                    fprintf(stderr, "Alokacia zlyhala\n");
             }
            }
            
            break;
        }

        case 4: {
            if(strcmp(argv[1], "-n") != 0) {
                fprintf(stderr,"Zly argument programu\n");
                return -1;
            }
            
            char arg_number[63];
            strncpy(arg_number, argv[2], 64);
            if (arg_number[0] == '+') {
                mode = PLUS_MODE;
                arg_number[0]='0'; 
            }
            
            parsed_nmbr = nmbr_parse(arg_number);
            if (parsed_nmbr == -1) {
                fprintf(stderr, "Zle zadany pocet riadkov\n");
                return -1;
            }


            f = fileopen(argv[3]);

            if (mode == PLUS_MODE){
                tail_2(f, parsed_nmbr);
            }
            else {
                char ** buffer = aloc_buffer(parsed_nmbr);
                if (buffer != NULL) {
                    tail(f, buffer, parsed_nmbr);
                    free_buffer(buffer, parsed_nmbr);
                }
                else{
                    fprintf(stderr, "Alokacia zlyhala\n");
             }
            }


            break;

            
        }


        default: {
            fprintf(stderr, "Nespravny pocet argumentov!\n");
            return -1;
            break;
        }
    }
    
    
  


    file_close(f);
    return 0;
    

   
}
