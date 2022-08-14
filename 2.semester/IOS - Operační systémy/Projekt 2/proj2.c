#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/wait.h>
#include <sys/mman.h>



#define CLEAN_RESOURCES \
	do { \
        sem_destroy(sem_may_enter); \
        sem_destroy(sem_entered); \
		sem_destroy(sem_may_leave);		\
        sem_destroy(sem_left); \
		sem_destroy(sem_decision); \
		sem_destroy(sem_registration);		\
        sem_destroy(sem_log);	\
        sem_destroy(sem_guard);	\
		sem_destroy(sem_process_finished);	\
        \
		munmap(sem_may_enter, sizeof(sem_t));			\
        munmap(sem_entered, sizeof(sem_t));			\
		munmap(sem_may_leave, sizeof(sem_t));		\
        munmap(sem_left, sizeof(sem_t));		\
		munmap(sem_decision, sizeof(sem_t));		\
		munmap(sem_registration, sizeof(sem_t));		\
        munmap(sem_log, sizeof(sem_t));	\
        munmap(sem_guard, sizeof(sem_t));	\
		munmap(sem_process_finished, sizeof(sem_t));	\
        \
	    munmap(A, sizeof(int)); \
        munmap(I, sizeof(int)); \
        munmap(NO_JUDGE, sizeof(int)); \
        munmap(REG_WAITING, sizeof(int)); \
        munmap(ENTERING, sizeof(int)); \
        munmap(NE, sizeof(int)); \
		munmap(NC, sizeof(int)); \
		munmap(NB, sizeof(int)); \
		munmap(R, sizeof(int)); \
		munmap(LEAVING, sizeof(int)); \
		munmap(RO, sizeof(int)); \
	} while (0)


int arg_parse(char * nmbr){
    char *buffer = NULL;
    int number = strtol(nmbr, &buffer, 10);
    if(!*buffer){
        if (number < 0){
            return -1;
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


int main(int argc, char **argv){


    //spracovanie argumentov
    
    int PI = 0; //počet vygenerovaných migrantov
    int IG = 0; // max doba (v ms), po ktorej sa vygeneruje novy migrant 
    int JG = 0; //max doba (v ms), po ktorej sa sudca vrati do budovy
    int IT = 0; //max doba (v ms) trvania vyzdvihnutia certifikatu
    int JT = 0; //max doba (v ms) vydania rozhodnutia sudom

    int error = 0;

    if (argc == 6 ){
        PI = arg_parse(argv[1]);
        if(PI == -1 || PI < 1){
            error++;
        }
        
        IG = arg_parse(argv[2]);
        if(IG == -1 || IG > 2000){
            error++;
        }
        IG = IG * 1000;
        JG = arg_parse(argv[3]);
        if(JG == -1 || JG > 2000){
            error++;
        }
        IT = arg_parse(argv[4]);
        if( IT == -1 || IT > 2000){
            error++;
        }
        IT = IT * 1000;

        JT = arg_parse(argv[5]);
        if(JT == -1 || JT > 2000){
            error++;
        }
        JT = JT * 1000;

        if(error > 0){

            fprintf(stderr, "Wrong arguments\n");
            return 1;

        }




    }
    
    else {
        fprintf(stderr, "Wrong number of arguments\n");
        return 1;
    }



    /*** zaciatok kodu ***/


    FILE * f = fopen("proj2.out", "wb");
    if (f == NULL) {
        fprintf(stderr, "Error opening file\n");
        return 1;
    }

    //prevencia bufferingu
    setbuf(stderr, NULL);
    setbuf(f, NULL);
    

    srand(time(0));



    //vygenerovanie semaforov a zdielanej pamete

    sem_t *sem_may_enter; 
    sem_t *sem_entered; 
	sem_t *sem_may_leave; 
    sem_t *sem_left;
	sem_t *sem_registration; 
    sem_t *sem_decision; 
	sem_t *sem_log;
    sem_t *sem_guard; 
    sem_t *sem_process_finished; 
        
    sem_may_enter = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    sem_entered = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0); 
	sem_may_leave = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    sem_left = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);  
	sem_registration = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0); 
	sem_decision = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0); 
	sem_log = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0); 
    sem_guard = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);  
    sem_process_finished = mmap(NULL, sizeof(sem_t), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0); 
        
	sem_init(sem_may_enter, 1, 0);
    sem_init(sem_entered, 1, 0);  
	sem_init(sem_may_leave, 1, 0); 
    sem_init(sem_left, 1, 0); 
	sem_init(sem_registration, 1, 0); 
	sem_init(sem_decision, 1, 0); 
	sem_init(sem_log, 1, 1); 
    sem_init(sem_guard, 1, 1); 
    sem_init(sem_process_finished, 1, 0);  

    int *A; 
    int *I; 
    int *NO_JUDGE; 
    int *REG_WAITING; 
    int *ENTERING; 

    int *NE; 
    int *NC; 
    int *NB; 
    int *R; 
	int *LEAVING;  
	int *RO; 
    


    A = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    I = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    NO_JUDGE = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    REG_WAITING = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    ENTERING = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    NE = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	NC = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	NB = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    R = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	LEAVING = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
	RO = (int*)mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    *A = 1;
    *I = 0;
    *NO_JUDGE = 0;
    *REG_WAITING = 0;
    *ENTERING = 0;
    *NE = 0;
    *NC = 0;
    *NB = 0;
    *R = 0;
	*LEAVING = 0;
	*RO = 0;

    int mainPid;
	int immPid;
	int judgePid;

    int waiting_for_decision;


    if ((mainPid = fork()) < 0)
	{
		CLEAN_RESOURCES;
        file_close(f);
		fprintf(stderr, "Error in main fork\n");
		exit(1);
	}


    if (mainPid == 0)	
	{   
    
		for (int k = 0; k < PI; k++)
		{	
			if (IG > 0){
                usleep(rand() % IG);
            }
			

           
			if ((immPid = fork()) < 0)
			{
				CLEAN_RESOURCES;
                file_close(f);


				fprintf(stderr, "Error in fork for immigrants\n");
				exit(1);
			}
			
             //proces jednotlivych imigrantov
			if (immPid == 0)
			{
                
				
				int id = 0;
                sem_wait(sem_log);
                *I+= 1;
                id = *I;
                fprintf(f, "%d\t\t: IMM %d\t\t\t: starts\n", *A, id);
                *A+=1;
                sem_post(sem_log);

                //pokial je v miestnost sudca, caka na jeho odchod
                if (*NO_JUDGE == 1){
                    sem_wait(sem_log);
                    *ENTERING+=1;

                    sem_post(sem_log);
					sem_wait(sem_may_enter); 
                    
                    sem_post(sem_entered);
                    
				}
                
                
                sem_wait(sem_log);
                *NE+=1;
                *NB+=1;
				fprintf(f, "%d\t\t: IMM %d\t\t\t: enters\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, id, *NE, *NC, *NB);
                *A+=1;
                sem_post(sem_log);

                

                sem_wait(sem_log);
                *NC+=1;
                fprintf(f, "%d\t\t: IMM %d\t\t\t: checks\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, id, *NE, *NC, *NB);
                *A+=1;
                sem_post(sem_log);


                //pokial sa nestihli vsetci doregistrovat
                if (*REG_WAITING != 0 && *NE == *NC){
                sem_post(sem_registration);} 

                //caka na rozhodnutie sudcu
                sem_wait(sem_decision);


                sem_wait(sem_log);
                fprintf(f, "%d\t\t: IMM %d\t\t\t: wants certificate\t\t: %d\t\t: %d\t\t: %d\n", *A, id, *NE, *NC, *NB);
                *A+=1;
                sem_post(sem_log);

                //caka na vydanie certifikatu
                if (IT > 0){
                    usleep(rand() % IT);
                }
                


                sem_wait(sem_log);
                fprintf(f, "%d\t\t: IMM %d\t\t\t: got certificate\t\t: %d\t\t: %d\t\t: %d\n", *A, id, *NE, *NC, *NB);
                *A+=1;
                sem_post(sem_log);

                //pokial je pri odchode v miestnosti sudca, caka na jeho odchod
                if (*NO_JUDGE == 1){
                    sem_wait(sem_log);
                    *LEAVING+=1;
                    sem_post(sem_log);
					sem_wait(sem_may_leave); 
                    
                    sem_post(sem_left);
                }  

                sem_wait(sem_log);
                *NB-=1;
                fprintf(f, "%d\t\t: IMM %d\t\t\t: leaves\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, id, *NE, *NC, *NB);
                *A+=1;
                sem_post(sem_log);
                
			
				sem_post(sem_process_finished);
				exit(0);
			}
		}

		exit(0);
	}

    //sudca
    if ((judgePid = fork()) < 0)
	{
		CLEAN_RESOURCES;
        file_close(f);
		fprintf(stderr, "Error in main fork\n");
		exit(1);
	}

	if (judgePid == 0)
	{	
        //kym nerozhodne o vsetkych migrantoch
        while(*R != PI){     
	
            if (JG > 0){
                usleep(rand()%JG);
            }
            
            sem_wait(sem_log);
            fprintf(f, "%d\t\t: JUDGE \t\t: wants to enter\n", *A);
		    *A+=1;
            sem_post(sem_log);

            sem_wait(sem_log);
	        fprintf(f, "%d\t\t: JUDGE \t\t: enters\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, *NE, *NC, *NB);
		    *A+=1;
            *NO_JUDGE = 1;
            sem_post(sem_log);


            //pokial nie su vsetci zaregistrovani 
            if (*NE != *NC){
                sem_wait(sem_log);
		        fprintf(f, "%d\t\t: JUDGE \t\t: waits for imm\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, *NE, *NC, *NB);
                *REG_WAITING = 1;
                *A+=1;
                sem_post(sem_log);
                sem_wait(sem_registration); //doregistrovanie migranta
                *REG_WAITING = 0;
		    }

            //sudca vydava rozhodnutia
            sem_wait(sem_log);
		    fprintf(f, "%d\t\t: JUDGE \t\t: starts confirmation\t: %d\t\t: %d\t\t: %d\n", *A, *NE, *NC, *NB);
            *A+=1;
            sem_post(sem_log);
            if (JT > 0){
                usleep(rand()%JT);
            }


            waiting_for_decision = *NC;
            sem_wait(sem_log);
            *NE = 0;
            *NC = 0;
            sem_post(sem_log);
            sem_wait(sem_log);
		    fprintf(f, "%d\t\t: JUDGE \t\t: ends confirmation\t\t: %d\t\t: %d\t\t: %d\n", *A, *NE, *NC, *NB);
            *A+=1;
            sem_post(sem_log);

            //vyda potvrdenia zaregistrovanym migrantom
            for(int i = 0; i < waiting_for_decision; i++){
			sem_post(sem_decision);
            *R+=1;   
		    }

            //odchod z budovy
            if (JT > 0){
                usleep(rand()%JT);
            }
            

            sem_wait(sem_log);
	        fprintf(f, "%d\t\t: JUDGE \t\t: leaves\t\t\t\t: %d\t\t: %d\t\t: %d\n", *A, *NE, *NC, *NB);
		    *A+=1;
            *NO_JUDGE = 0;
            sem_post(sem_log);
 
            //povoli vstup kazdemu, kto sa pokusa vojst
            while(*ENTERING != 0){
                sem_post(sem_may_enter);
                sem_wait(sem_entered);
                sem_wait(sem_log);
                *ENTERING -=1; 
                sem_post(sem_log);
            }

            //povoli odchod kazdemu, kto sa pokusa odist
            while(*LEAVING != 0){
                sem_post(sem_may_leave);
                sem_wait(sem_left);
                sem_wait(sem_log);
                *LEAVING -=1;
                sem_post(sem_log); 
            }

           
        }

        //po rozhodnuti o vsetkych mirantoch
        sem_wait(sem_log);
            fprintf(f, "%d\t\t: JUDGE \t\t: finishes\n", *A);
		    *A+=1;
            sem_post(sem_log);


   
		sem_post(sem_process_finished);

		exit(0);
	}


    //hlavny proces skonci po skonceni vsetkych pomocnych (migranti + sudca)
	for (int i = 0; i < PI + 1; i++)
		sem_wait(sem_process_finished);

	
	CLEAN_RESOURCES;
    file_close(f);
	exit(0);

}




