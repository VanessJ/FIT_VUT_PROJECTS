// # ppm.h
// # Riešenie IJC-DU1 b), 17.3.2020
// # Autor: Vanessa Jóriová, xjorio00, VUT FIT
// # Preložené: gcc 7.4.0
// # Zostavenie: IJC-DU1

#ifndef PPM_H
#define PPM_H

#define SIZE_LIMIT (8000 * 8000 *3)

struct ppm {
    unsigned xsize;
    unsigned ysize;
    char data[];
};

struct ppm * ppm_read(const char *filename);
void ppm_free(struct ppm *p);

#endif
