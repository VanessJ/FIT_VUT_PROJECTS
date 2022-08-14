					/************************************************************/
					/*			Vanessa Jóriová			    */
					/*			     xjorio00		            */	
					/*			     27.11.2019		            */
					/*			     Projekt 2		            */
					/************************************************************/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define I0 1e-12					//konstanta vyplyvajuca zo zadania
#define Ut 0.0258563					//konstanta vyplyvajuca zo zadania



							//prototypy funkcii
double f (double x, double U0, double R);
double diode (double u0, double r, double eps);
double IP (double UP);

		

						//v pripade poctu argumentov <4 je program ukonceny chybovym hlasenim
						
int  main(int argc, char *argv[]) {
char *end;
if (argc == 4) {
						/*pre nacitanie vstupu sa pouziva funkcia strtod(), ktora do premenej nacita cast 
						 cisla konvertovatelnu na double a nastavi pointer na zaciatok retazca nekonvertovatelnych
						 znakov. Pre spravnost vstupu sa predpoklada, ze dany argument obsahuje znaky,
						 tvoria ho  len konvertovatelne znaky a konvertovana hodnota nema zapornu hodnotu, 
						 v pripade R nulu. */
	double U0 = strtod(argv[1], &end);
	if (argv[1][0]== '\0' || *end != '\0' || U0 < 0){ fprintf(stderr, "error: invalid arguments\n"); return 1;}
	double R = strtod(argv[2], &end);	
	if (argv[2][0]== '\0' || *end != '\0' || R <= 0){ fprintf(stderr, "error: invalid arguments\n"); return 1;}
	double EPS = strtod(argv[3], &end);
	if (argv[3][0]== '\0' || *end != '\0' || EPS <= 0){ fprintf(stderr, "error: invalid arguments\n"); return 1;}
	if(EPS <= 1e-15) EPS = 1e-15;
 	double UP = diode(U0, R, EPS);
	fprintf(stdout, "Up = %g V\n", UP);
	fprintf(stdout, "Ip = %g A\n", IP(UP));
}
else 
	{fprintf(stderr, "Not enough arguments\n");
	 return 1;}
return 0;
}


/**
 * @brief Funkcia hlada hodnotu Up
 * @details Funkcia hladajuca hodnotu Up pomocou metody bisekcie. Pociatocny interval tvoria hodnoty 0.0 a U0, 
 	    tento interval sa nasledne zmensuje, az kym nevyhovie zadanej odchylke
 * @param U0 Vstupny prud
 * @param R  Napatie 
 * @param EPS Odchylka
 * @return Up Napatie pracovneho bodu diody */

double diode (double u0, double r, double eps){
	double a = 0.0;
	double b = u0;
	double middle = (a + b)/2;
	double fmid = f(middle, u0, r);
//	printf("Middle na zaciatku %g a fmid %g\n", middle, fabs(fmid));
	while (fabs(b-a) >=eps) {
		if (f(a, u0, r) * fmid < 0) 
			b = middle;
		else 
		a = middle;
	//printf("Novy middle je: %g \n",  middle);
		if (fabs (b-a) >= eps) {
		middle = (a+b)/2;
		fmid = f(middle, u0, r);
		}
//	printf("Dalsi middle je %g a fmid %g \n", middle, fabs(fmid));
	}
	return middle;
}
 
/**
 * @brief Odvodena rovnica pre vypocet Up
 * @param x  Stredova hodnota intervalu
 * @param U0  Vstupne napatie
 * @param EPS Odchylka
 * @return Hodnota pre dany interval*/
double f(double x, double U0, double R) {
	return I0 * (exp(x/Ut)-1)-(U0-x)/R;
}

/**
 * @brief Rovnica pre vypocet Ip - pracovneho prudu diody
 * @param Up  Napatie pracovneho bodu diody
 * @return Hodnota Ip */

double IP(double Up) {
	return I0 * (exp(Up/Ut)-1);
}

