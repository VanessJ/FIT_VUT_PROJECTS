					/************************************************************/
					/*			Vanessa Jóriová	                    */
					/*			     xjorio00		            */	
					/*			     27.11.2019		            */
					/*			     Projekt 3		            */
					/************************************************************/




#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//struktura pre ukladanie mapy bludiska  
typedef struct {
	int rows;			//pocet riadkov bludiska
	int cols;			//pocet stlpcov bludiska
	unsigned char *cells;		//informacie o ciselnom popise jednotlivych policok
}Map;

enum border {LEFT, RIGHT, HORIZONTAL}; 	//priradenie ciselnej hodnoty jednotlivym stranam podla bitu, ktory ich popisuje
#define EXIT_SUCCES 0
#define EXIT_FAILURE 1
#define LPATH -1
#define RPATH 1

//prototypy funkcii
void help();
void free_map(Map *map);
int get_number(char *s);
void load(char *filename, Map *map);
int map_check(char *filename);
bool isborder(Map *map, int r, int c, int border);
int valid_border(Map *map);	
int valid_entrance(Map *map, int r, int c);
int start_border(Map *map, int r, int c, int leftright);
int find_direction(Map *map, int r, int c, int leftright);
void move(int *r, int *c, int *direction, int leftright);
int buffer_size(char *buffer);

int main(int argc, char *argv[]) {
	Map map;
	int leftright, r, c, loaded;
	char filename[300];
	if (argc==2) {
			if((strcmp(argv[1], "--help"))==0) {
				help();
				return(EXIT_SUCCES);}
			}
	
	if (argc==3) {
			if((strcmp(argv[1], "--test"))==0){
				strcpy(filename, argv[2]);
				if (map_check(filename)==0){
					load(filename, &map); loaded = 1;
					if (valid_border(&map)==0){
						fprintf(stdout, "Valid\n");	
						free_map(&map);
						return EXIT_SUCCES;}
						} 
			if(map_check(filename)==-2){
				fprintf(stderr, "Error reading file\n");
				return (EXIT_FAILURE);}
				
				fprintf(stdout, "Invalid\n");
				if (loaded==1) free_map(&map);
				return(EXIT_SUCCES);}
		     }
	
	if(argc==5) {
			int validity = 0;
	
			if((strcmp(argv[1], "--rpath"))==0) {
				leftright = RPATH; 
				validity++;}
			if ((strcmp(argv[1], "--lpath"))==0)
				{leftright = LPATH; 
				validity++;}
			if(get_number(argv[2])!=-1 && get_number(argv[3]) !=-1) {
				r=get_number(argv[2]);	
				c=get_number(argv[3]);
				validity++;}
			if (validity ==2) {	
				strcpy(filename, argv[4]);
				if (map_check(filename)==0){
					--r;
					--c;
					 load(filename, &map); loaded = 1; 
					 if (valid_border(&map)==0){
						if (valid_entrance(&map, r, c) !=0) {
							fprintf(stderr, "Unable to enter the maze from this position\n");
							free_map(&map);
							return EXIT_FAILURE;}
						if (start_border(&map, r, c, leftright)<0){
							fprintf(stderr, "Unable to enter the maze due to blocked entrance\n");
							free_map(&map); 
							return EXIT_FAILURE;}

						find_direction(&map, r, c, leftright);
						free_map(&map);
						return EXIT_SUCCES;} }
				
			fprintf(stderr,"Invalid map format\n");
			if (loaded==1) free_map(&map);
			return EXIT_FAILURE;
			} 
			}
		
		fprintf(stderr, "Invalid arguments! For more info see --help\n");
		return EXIT_FAILURE;
		}


void free_map(Map *map) {
	free(map->cells);
	map->cells = NULL;
	}
	
//rozhodne, ci nacitany string obsahuje prave jedno cislo konvertovatelne do int

int get_number(char *s){
	char *ptr;
	int number = strtol(s, &ptr, 10);
	if(*ptr!='\0') return -1;
	else if (number<=0) return -1;
	return number;
}


/**
 *@brief Funkcia s vypisom pokynov pre uzivatelov
 * */


void help() {
	const char *help = "\n	Projekt 3 - priechod bludiskom\n"
			   "Program vypise suradnice cesty von z bludiska podla zvoleneho pravidla navigacie bludiskom.\n"
			   "\nSpustanie programu:\n"
			   "\n--help: program zobrazi napovedu.\n"
			   "\n--test subor.txt: program skontroluje, ci sa v subore nachadza korektny zapis bludiska.\n"
			   "Korektny zapis v prvom riadku obsahuje dve lubovolne cisla popisujuce pocet riadkov a stlpcov programu(v tomto poradi).\n"
			   "Nasleduje ciselny popis jednotlivych policok. Cisla od 1 do 7 popisuju hrany jednotlivych policok.\n"
			   "Cisla musia byt oddelene bielymi znakmi a na pozicii policka, ktore reprezentuju.\n"
			   "Pri splneni tychto kriterii vypise program Valid, v opacnom pripade vypise invalid.\n"
			   "\n--rpath R C subor.txt: vypise suradnice cesty von z bludiska podla pravidla pravej ruky.\n"
			   "R a C predstavuju suradnice vstupneho policka (riadok a stlpec), subor zase subor obsahujuci korektnu mapu bludiska.\n"
			   "\n--lpath R C subor.txt: Hlada cestu podla pravidla lavej ruky. Parametre su rovnake ako v predoslom pripade.\n";
	printf("%s", help);
}




/**
 * @brief Funkcia meniaca suradnice a hranu, ktoru sledujeme podla prislusnej ruky
 *@details Na zaklade pravidla pre navigaciu bludiskom a orientacie daneho trojuholnika prislusne zmeni danu suradnicu 
	   a hranicu, ktorej sa chytime 
 *@param int *x Suradnica riadku daneho policka
 *@param int *y Suradnica stlpca daneho policka 
 *param int *direction Smer, ktorym sa pohybujeme vzhladom na stenu trojuholnika
 *@param leftright Pravidlo pohybu podla ruky, ktore sme zvolili **/


void move(int *x, int *y, int *direction, int leftright){
	int a = *x +1;
	int b = *y +1;
	fprintf(stdout,"%d,%d\n", a, b);
	int sum= (*x + *y)%2;
	if(leftright==RPATH){
		if (sum==0) {
			if (*direction==LEFT){
				(*y)--;
				*direction=LEFT;}
			else if(*direction==HORIZONTAL){
				(*x)--;
				*direction=RIGHT;}
			else if(*direction==RIGHT){
				(*y)++;
				*direction=HORIZONTAL;}
			}
		if(sum!=0){	
			if (*direction==LEFT){
				(*y)--;
				*direction=HORIZONTAL;}
			else if(*direction==HORIZONTAL){
				(*x)++;
				*direction=LEFT;}
			else if(*direction==RIGHT){
				(*y)++;
				*direction=RIGHT;}
		 
		}
		}

	
	if(leftright==LPATH){
		if (sum==0) {
			if (*direction==LEFT){
				(*y)--;
				*direction=HORIZONTAL;}
			else if(*direction==HORIZONTAL){
				(*x)--;
				*direction=LEFT;}
			else if(*direction==RIGHT){
				(*y)++;
				*direction=RIGHT;}
			}
		if(sum!=0){	
			if (*direction==LEFT){
				(*y)--;
				*direction=LEFT;}
			else if(*direction==HORIZONTAL){
				(*x)++;
				*direction=RIGHT;}
			else if(*direction==RIGHT){
				(*y)++;
				*direction=HORIZONTAL;}
		 
		}
		}
	

}



/**
 * @brief Funkcia hladajuca cestu von z bludiska
 *@details Na zaklade nami zvoleneho pravidla pre pohyb bludiskom podla ruky sa pokusi pohnut bludiskom. Pokial je dana stena 
	   zablokovana, zvoli dalsiu podla priority. Vyjdenie mimo suradnic bludiska sa povazuje za uspesny vychod z bludiska 
 *@param Map *map Struktura map obsahujuca udaje o bludisku
 *@param int r Suradnica riadku policka
 *param int c  Suradnica stlpca policka
 *@param leftright Pravidlo pohybu podla ruky, ktore sme zvolili
 *@return 0 v pripade uspesneho prechodu bludiskom, -1 v pripade nemozneho prechodu (zablokovany vstup) **/

	
int find_direction(Map *map, int r, int c, int leftright){
	int border = start_border(map, r, c,leftright);
	if (border ==-1) {
		return -1;
			 }
	while(r>=0&&r<map->rows && c>=0 && c<map->cols) {
		while(isborder(map, r, c, border)){
			if (leftright==RPATH) {		//(r+c)%2 vyjadruje orientaciu policka, !(r+c)%2 predstavuje trojuholnik otoceny nahor,
							//opacny pripad zasa trojuholnik otoceny nadol 				
				if((r+c)%2==0){
					if (border==HORIZONTAL)	
						border=LEFT;
					else if (border==LEFT)
						border=RIGHT;
					else if (border==RIGHT)	
						border=HORIZONTAL;
					}		
				if((r+c)%2!=0) {
					if(border==HORIZONTAL)	
						border=RIGHT;
					else if(border==RIGHT)
						border=LEFT;
					else if(border==LEFT)
						border=HORIZONTAL;
					}	
				}

			if (leftright==LPATH) {				
				if((r+c)%2==0){
					if (border==HORIZONTAL)	
						border=RIGHT;
					else if (border==LEFT)
						border=HORIZONTAL;
					else if (border==RIGHT)	
						border=LEFT;
					}		
				if((r+c)%2!=0) {
					if(border==HORIZONTAL)	
						border=LEFT;
					else if(border==RIGHT)
						border=HORIZONTAL;
					else if(border==LEFT)
						border=RIGHT;
					}	
				}

			}
				move(&r,&c, &border, leftright); 
		
		
		}
		
			return 0;
}


/**
 * @brief Funkcia vracajuca hranu trojuholnika, ktorej sa pri vstupe chytime 
 *@details Podla miesta vstupu v bludisku a zvoleneho pravidla urci hranicu, ktorej sa pri vstupe chytme  
 *@param Map *map Struktura map obsahujuca udaje o bludisku 
 *@param int r Suradnica riadku policka
 *param int c Suradnica stlpca policka
 *@param leftright Pravidlo pohybu podla ruky, ktore sme zvolili 
 *@return Strana trojuholnika alebo -1 v pripade, ked je vstup kvoli zablokovaniu policka hranami **/

int start_border(Map *map, int r, int c, int leftright) {
	if (leftright==RPATH) {
		if (c==0 && (r%2)==0) {		//vstup zlava na parnom riadku pri indexovani od 0
			if (!isborder(map, r, c, LEFT))
				return RIGHT; 
			}
		 if (c==0 && (r%2)!=0) { //zlava na neparnom pri indexovani od 0
			if (!isborder(map, r, c, LEFT))
				return HORIZONTAL;
			}
		 if (c==map->cols-1 && (r+c)%2==0) { //sprava, pokial smeruje trojuholnil dole
			if(!isborder(map,r, c, RIGHT))
				return HORIZONTAL;
			}
		if (c==map->cols-1 && (r+c)%2!=0){ //sprava, pokial smeruje trojuholnik hore
			if(!isborder(map, r, c, RIGHT))
				return LEFT;
			}
		if (r==0) {
			if(!isborder(map,r,c,HORIZONTAL)) //zhora
				return LEFT;
			}
		 if(r==map->rows-1) {
			if(!isborder(map, r, c, HORIZONTAL))//zdola
				return RIGHT;
			} 
	}

	if (leftright==LPATH) {

		if (c==0 && (r%2)==0) {		//vstup zlava na parnom riadku pri indexovani od 0
			if (!isborder(map, r, c, LEFT))
				return HORIZONTAL; 
			}
		if (c==0 && (r%2)!=0) { //zlava na neparnom pri indexovani od 0
			if (!isborder(map, r, c, LEFT))
				return RIGHT;
			}
		 if (c==map->cols-1 && (r+c)%2==0) { //sprava, pokial smeruje trojuholnil dole
			if(!isborder(map,r, c, RIGHT))
				return LEFT;
			}
		 if (c==map->cols-1 && (r+c)%2!=0){ //sprava, pokial smeruje trojuholnik hore
			if(!isborder(map, r, c, RIGHT))
				return HORIZONTAL;
			}
		 if (r==0) {
			if(!isborder(map,r,c,HORIZONTAL)) //zhora
				return RIGHT;
			}
		 if(r==map->rows-1) {
			if(!isborder(map, r, c, HORIZONTAL))//zdola
				return LEFT;
			} 
	}


			
	return -1;	}






/**
 * @brief Funkcia, ktora vracia, ci sa z danej pozicie da dostat do bludiska
 *@details Funkcia na zaklade suradnic r a c a tvaru mapy rozhodne, ci je vstup do bludiska z danej pozicie mozny (bez ohladu na steny) 
 *@param Map *map Struktura obsahujuca bludisko
 *@param int r Suradnica riadku policka 
 *@param int c Suradnica stlpca policka
 *@return 0 v pripade mozneho vstupu, 1 v pripade pokusu o vstup z policka, ktore vstup nepovoluje, alebo mimo bludiska **/
 



int valid_entrance(Map *map, int r, int c) {
	if(r==0) {
		if ((c==0) || (c==map->cols-1) || (c%2==0)) return 0;
	}
	if(r==map->rows-1) {
		if ((c==0) || (c==map->cols-1)) return 0;
		else if ((map->rows%2==0) && (c%2==0)) return 0;
				
		else if(map->rows%2!=1&& (c%2!=1))return 0;
							
			
 		}
		
	if(r!=0 && r!=map->rows-1) {
		if(c==0 || c==map->cols-1) return 0;

					

	} 	
		return 1;}
	


/**
 * @brief Funkcia, ktora rozhodne o spravnosti ciselnych popisov hran bludiska
 *@details Funkcia overi, ci sedia hrany bludiska - ci sa na rozhrani jednotlivych policok nachadza rovnaky typ hranice (pevna alebo priechodna) 
           Pokial ma policko pevnu hranu na pravej strane, overi sa, ci je pevna aj lava strana susedneho policka (podobne pre hornu a dolnu)
 *@param Map *map Struktura obsahujuca bludisko
 *@return 0 v pripade spravnych hranic, 1 v pripade nespravnych
 **/

int valid_border(Map *map) {
	int r; int c;
				//cyklus rozhodujuci o spravnosti pravej a lavej hranice policok 

	for(r=0; r<map->rows;r++) {
		c=0;
		if(isborder(map,r,c,RIGHT)==true && isborder(map, r,c+1,LEFT)!=true) {
			 return 1;}

		c=map->cols-1;
		if (isborder(map,r,c,LEFT)==true && isborder(map, r,c-1,RIGHT)!=true)	{
			return 1;}
		for (c=1; c<map->cols-1;c++) {
			if (isborder(map,r,c,RIGHT)==true && isborder(map, r,c+1,LEFT)!=true) {
				return 1;}
			if (isborder(map,r,c,LEFT)==true && isborder(map, r,c-1,RIGHT)!=true) {
				return 1;}

			

 		}}
	int i,j;
				//cyklus rozhodujuci o spravnosti hornych a dolnych hranic
	for(j=0;j<=map->rows-1;j++)
		for(i=0;i<map->cols-1;i++) {
			if (i%2 != j%2)
				if((j<map->rows-1)&&isborder(map,j,i, HORIZONTAL) !=isborder(map,j+1,i,HORIZONTAL)) {
				return 1;}}
	return 0;
}





/**
 * @brief Funkcia, ktora vracia, ci sa v danom trojuholniku na danej pozicii nachadza pevna hrana 
 *@details Podla ciselnej rerezentacie policka sa rozhodne, ci ma bit na pozicii ciselneho oznacenia hrany hodnotu jedna   
 *@param Map *map Struktura map obsahujuca udaje o bludisku 
 *@param int r Suradnica riadku policka
 *@param int c Suradnica stlpca policka
 *@return True v pripade, ze je hranica pevna, false v pripade, ze je hranica priechodna
 **/





bool isborder(Map *map, int r, int c, int border){
	int bitstatus = (*(map->cells+r*map->cols+c)>>border)&1;
	if (bitstatus==1) return true;
	else return false;
	} 


/**
 * @brief Funkcia, ktora overi korektnost zadanej mapy 
 *@details Funkcia skontroluje, ci subor existuje a da sa otvorit, dalej rozhodne, ci je mozne precitat jednotlive znaky,
	   ci rozmery bludiska sedia zadanemu popisu a ci policka obsahuju vhodne popisy hran
 *@return 0 v pripade vhodneho suboru, -1 v pripade nevhodneho  
 **/

int map_check(char *filename) {
	FILE *f;
	f = fopen(filename, "r+");
	if (f==NULL) {
		return -2;}
	int rows,cols,size;
	char buffer[102];
	unsigned char number;
	if (fscanf(f, "%d %d", &rows, &cols)!=2){
		fclose(f); 
		return -1;}
	fgets(buffer, 100, f);
	size = strlen(buffer);
	if(size>1){
		fclose(f);
		return -1;}
	int i, j;

	for(i=0;i<rows; i++){
		for(j=0;j<cols;j++) {
			if(fscanf(f, "%hhu", &number)!=1) {
				fclose(f);
				return -1;}
			if(number>7) {
				fclose(f);
				return -1;}
		}
	}

	//pomocou fgets nacita zvysny obsah aktualneho aj dalsieho riadku a presvedci sa, ze neobsahuje dalsie znaky
	fgets(buffer,100,f);
	if(buffer_size(buffer)!=0){
		fclose(f);
		return -1;}	
	fgets(buffer,100,f);
	if(buffer_size(buffer)!=0){
		fclose(f);
		return -1;}
	

	fclose(f);
	return 0;
}
	
int buffer_size(char *buffer) {
	int size = strlen(buffer);
	if (size>1) return 1;
	return 0;

}




/**
 * @brief Funkcia, ktora nacita strukturu map 
 *@details Funkcia nacita pocet riadkov a stlpcov do struktury a cislo reprezentujuce jednotlive policka do pola    
 *@param Map *map Struktura map obsahujuca udaje o bludisku 
  **/

void load(char *filename, Map *map) {
	FILE *f;
	unsigned char number;
	f = fopen(filename, "r+");
	fscanf(f,"%d %d", &map->rows, &map->cols);
	if ((map->cells=(unsigned char *)malloc(map->rows * map->cols *sizeof(unsigned char)))==NULL) {
		fprintf(stderr, "Memory allocation unsuccesful\n");
		fclose(f);
		exit(-1);}
	char buffer[102];
	fgets(buffer, 100,f);
	int i,j;
	for (i=0; i<map->rows; i++) {
		for (j=0; j < map->cols;j++) {
			fscanf(f, "%hhu", &number);
			*(map->cells+i*map->cols+j) = number;}
		}
	fclose(f);
	}



 
