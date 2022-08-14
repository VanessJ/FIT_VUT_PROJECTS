//======== Copyright (c) 2017, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Test Driven Development - priority queue code
//
// $NoKeywords: $ivs_project_1 $tdd_code.cpp
// $Author:     Vanessa Jóriová <xjorio00@stud.fit.vutbr.cz>
// $Date:       $2020-03-04
//============================================================================//
/**
 * @file tdd_code.cpp
 * @author Vanessa Jóriová
 * 
 * @brief Implementace metod tridy prioritni fronty.
 */

#include <stdlib.h>
#include <stdio.h>

#include "tdd_code.h"

//============================================================================//
// ** ZDE DOPLNTE IMPLEMENTACI **
//
// Zde doplnte implementaci verejneho rozhrani prioritni fronty (Priority Queue)
// 1. Verejne rozhrani fronty specifikovane v: tdd_code.h (sekce "public:")
//    - Konstruktor (PriorityQueue()), Destruktor (~PriorityQueue())
//    - Metody Insert/Remove/Find a GetHead
//    - Pripadne vase metody definovane v tdd_code.h (sekce "protected:")
//
// Cilem je dosahnout plne funkcni implementace prioritni fronty implementovane
// pomoci tzv. "double-linked list", ktera bude splnovat dodane testy 
// (tdd_tests.cpp).
//============================================================================//

PriorityQueue::PriorityQueue()
{
    root = NULL;

}

PriorityQueue::~PriorityQueue()
{ 

    struct Element_t * Root_Element = root;
    while(Root_Element != NULL) {
        struct Element_t * Temp_Element = Root_Element;
        Root_Element = Root_Element->pNext;
        free(Temp_Element);
    }
}

void PriorityQueue::Insert(int value)
{ 
    struct Element_t * Current_Element;
    struct Element_t * Prev_Element = NULL;
   
    struct Element_t * New_Element = (struct Element_t *) malloc(sizeof(struct Element_t));
	New_Element -> value = value;

	if (root == NULL) {
		root = New_Element;
		New_Element -> pNext = NULL;
		New_Element -> pPrev = NULL;
        return; 
    }

    
    for (Current_Element = root; Current_Element != NULL; Current_Element = Current_Element -> pNext) {
        if (Current_Element -> value >= value) {
				break;
			}

        Prev_Element = Current_Element;
    }  
        
    if(Current_Element == NULL) {
        New_Element -> pPrev = Prev_Element;
		New_Element -> pNext = Current_Element;
		Prev_Element -> pNext = New_Element;
        return;
    }

            New_Element -> pPrev = Prev_Element;
		    New_Element -> pNext = Current_Element;
			
            if (Current_Element->pPrev == NULL) {
                root = New_Element;
			}
			
            else {
                Prev_Element -> pNext = New_Element;
			}

			Current_Element -> pPrev = New_Element;
} 



bool PriorityQueue::Remove(int value)
{   
	struct Element_t *Current_Element;

    bool found = false;

	for(Current_Element = root; Current_Element != NULL; Current_Element = Current_Element -> pNext){
		if (Current_Element->value == value){
            found = true;
            break;
		}

	}

    if (found == false) {
    return false;    
    }
    
    struct Element_t * Prev_Element = Current_Element -> pPrev;
    struct Element_t * Next_Element = Current_Element -> pNext;
    
    if (Current_Element->pNext != NULL){
				Next_Element->pPrev = Current_Element->pPrev;
			}

			if (Current_Element->pPrev != NULL){
				Prev_Element->pNext = Current_Element->pNext;
			}
			else{
				
                root = Current_Element->pNext;
			}

			free(Current_Element);
			return true;
}

PriorityQueue::Element_t *PriorityQueue::Find(int value)
{
    struct Element_t * Current_Element = root;

    while( Current_Element != NULL ) {
        if ( Current_Element -> value == value ) {
         return Current_Element;   
        }
        Current_Element = Current_Element -> pNext;
        
    }
    return NULL;
}

PriorityQueue::Element_t *PriorityQueue::GetHead()
{
    return root;

} 


/*** Konec souboru tdd_code.cpp ***/
