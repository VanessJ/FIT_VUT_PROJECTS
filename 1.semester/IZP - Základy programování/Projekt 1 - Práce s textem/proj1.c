/*****************************************************/
/*		Vanessa Jóriová			     */
/*		 13.11. 2019                         */
/*		    Proj1			     */
/*****************************************************/

//pouzite kniznice
#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <ctype.h>

/*102= 100 znakov + enter + '\0' */ 
const int MAX = 102;

//prototypy pouzitych funkcii
void convert (char *string);
int search(char *string, char *substring);
int length_check(char *string);
void write(char *name, char *number);

/*
 * Main nacitava z textoveho suboru dvojicu dvoch riadkov a vyhodnocuje ju
 * V pripade nepovoleneho formatu textoveho suboru program konci chybovym hlasenim  
 */

int main (int argc, char *argv[]){
	//deklaracia pouzitych premennych
	char name[MAX];
	char number[MAX];
	char name_copy[MAX]; 
	int match_nmbr = 0;

	while(fgets(name, MAX, stdin)!=NULL) { //nacita prvy z riadkov, meno  
		if(length_check(name)<0) return -1; //v pripade dlhsieho nez povoleneho riadku program skonci	 
			
		strcpy(name_copy,name); //kopia mena ulozena pre ucely vypisu
		convert(name);

	

	/*v pripade chybania paroveho riadku program skonci*/

		if (fgets(number, MAX, stdin) == NULL){ 
			fprintf(stderr, "Nekorektny zoznam - neparny pocet riadkov!\n");
			return -1;}
		else {
			if(length_check(number)<0) return -1;	
		if (argc<2) { //pri nezadani argumentu sa predpoklada, ze hladaniu vyhovuju vsetky kontakty a pristupuje sa k vypisu
			write(name_copy, number);
			}
		else {
		
			if ((search(name,argv[1]) !=0) || (search(number,argv[1])!=0)) {
				write(name_copy,number);
				match_nmbr++;
			}
		}
		}	
	} 

	if ((match_nmbr==0) && (argc >1)){ //v pripade nenajdenia zhody so zadanym argumentom 
		fprintf(stdout, "Not found.\n");
		} 
return 0;
}


/*Kontroluje ukoncenost nahraneho stringu, string dlhsi ako 100 znakov = neukonceny
 * @param string Nahrany riadok
 * vracia -1 v prípade neukonceneho stringu, 0 v pripade ukonceneho
 */
int length_check(char *string) {
if(strchr(string, '\n') ==NULL) { //Pokial sa v stringu nenachadza enter, znak sa nenacital cely - presahuje zadany limit	 
			fprintf(stderr, "Viac ako 100 znakov na riadku!\n");	
			return -1;}
else return 0;}




/*Vypise meno a cislo v pozadovanom formate
 * @param name Nahrane meno
 * @param number Nahrane cislo
 */
void write(char *name, char *number)
{	name[strlen(name)-1]=(int)','; //znak na danej pozicii, enter, sa prepise na pozadovany znak (ciarka)
	printf("%s %s", name, number);

}




/*Hlada zhodu zadaneho substringu v hlavnom stringu
 *@param string Nacitane meno (konvertovane na cisla
 *@param substring Nacitana postupnost znakov z argv[]
 * return 1 v pripade zhody, 0 v pripade nenajdenia zhody
 * nacita cislo z postupnosti a porovna ho so znakmi
 */

int search(char *string, char *substring){
	int size = strlen(substring);
	int i, j;
	int loops = 0; //pocet pismen, pre ktore sme kontrolovali zhodu
	int match = 0; //pocet najdenych zhod pre jednotlive pismena
	int boundary = 0; //posuvna hranica, od ktorej sa kontroluju znaky v stringu
	int checked  = 0; //pocet prekontrolovanych pismen hlavneho stringu
	while (loops!=size) {
		for (i=0;i<size;i++) {
			for (j=boundary; j<strlen(string);j++){
				if(substring[i] ==string[j] ){
					match++; 
					checked++;
					boundary = checked; /*startovny index sa posunie za miesto hladaneho znaku, aby sa dodrzala vzajomna postupnost
								znakov*/ 
					break;}
				checked++;
				}
			loops++; //ukocenie hladania zhody pre dane cislo 
		}
	}

	if (match==size) { //zhoda musi byt najdena pre kazde pismeno
		return 1; 
		}
	else {
	return 0;}
}




/* Konvertuje string pismen na string s korespondujucimi ciselnymi hodnotami
 * @param string Nacitane meno
 */

void convert(char *string)
{
	int i;
	for(i=0;i<strlen(string);i++) {
		char c;
		c = string[i];
		c = toupper(c); //v ramci redukcie switchu sa prevedu vsetky pismena na velke
		switch(c) {
			case 'A':
			case 'B':
			case 'C':
				c = '2';
				break;
			case 'D':
			case 'E':
			case 'F':
				c = '3';
				break;
			case 'G':
			case 'H':
			case 'I':
				c = '4';
				break;
			case 'J':
			case 'K':
			case 'L':
				c = '5';
				break;
			case 'M':
			case 'N':
			case 'O':
				c = '6';
				break;
			case 'P':
			case 'Q':
			case 'R':
			case 'S':
				c = '7';
				break;
			case 'T':
			case 'U':
			case 'V':
				c = '8';
				break;
			case 'W':
			case 'X':
			case 'Y':
			case 'Z':
				c = '9';
				break;
			case '+':
				c = '0';
				break;
			default: 			//neznamy znak sa nenahradza ziadnou ciselnou hodnotou
				break;
			}
			string[i] = c; 	
		}}

