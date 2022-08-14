// # ppm.c
// # Riešenie IJC-DU1 b), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1
// # Popis: skontroluje správnosť a načíta potrebné údaje z ppm obrázka

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ppm.h"
#include "error.h"

struct ppm * ppm_read(const char * filename) {
    FILE *fp;
    char format[3];
    unsigned xsize, ysize;
    int color;



    fp = fopen(filename, "r");
    if (fp == NULL){
        warning_msg("Subor %s sa nepodarilo otvorit.\n", filename);
        return NULL;
    }

    if(fscanf(fp, "%2s %u %u %d", format, &xsize, &ysize, &color) != 4 ){
        warning_msg("Nespravne zadana hlavicka suboru '%s'.\n", filename);
        fclose(fp);
        return NULL;
    }
    

    if (strcmp(format, "P6") != 0){
        warning_msg("Nespravny format suboru '%s'\n", filename);
        fclose(fp);
        return NULL;
  }

    if (color < 0 && color > 255){
		warning_msg("Nespravny rozsah farieb v subore '%s' \n");
        fclose(fp);
		return NULL;
	}

    size_t ppm_size = (3 * xsize * ysize);

    if (ppm_size > SIZE_LIMIT){
        warning_msg("Prilis velke rozmery obrazka.\n");
        fclose(fp);
        return NULL;
    }
        
        
    //struct ppm *pic = malloc(sizeof(struct ppm) + ppm_size);
    struct ppm *pic = malloc(sizeof(struct ppm) + (ppm_size * sizeof(char)));
    if (pic == NULL){
        warning_msg("Alokacia sa nepodarila.\n");
        fclose(fp);
        return NULL;
    }

    
    if(fread(pic->data, sizeof(char), ppm_size, fp) != ppm_size){
        warning_msg("Nepodarilo se nacist data ze souboru: '%s'.\n", filename);
        fclose(fp);
        free(pic);
        return NULL;
    }

    pic->xsize=xsize;
    pic->ysize=ysize;

    fclose(fp);

    return pic;

}

void ppm_free(struct ppm *p){
    free(p);
}



