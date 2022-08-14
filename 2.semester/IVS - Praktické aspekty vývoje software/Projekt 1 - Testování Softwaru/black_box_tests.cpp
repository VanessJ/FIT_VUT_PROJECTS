//======== Copyright (c) 2017, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     Red-Black Tree - public interface tests
//
// $NoKeywords: $ivs_project_1 $black_box_tests.cpp
// $Author:     Vanessa Jóriová <xjorio00@stud.fit.vutbr.cz>
// $Date:       $2020-03-04
//============================================================================//
/**
 * @file black_box_tests.cpp
 * @author Vanessa Jóriová
 * 
 * @brief Implementace testu binarniho stromu.
 */

#include <vector>

#include "gtest/gtest.h"

#include "red_black_tree.h"


class EmptyTree : public ::testing::Test
{
protected:

    BinaryTree binaryTree;
    
};


class NonEmptyTree : public ::testing::Test
{
protected:
    
    virtual void SetUp() {
        int values[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

        for(int i = 0; i < 12; ++i) {
            binaryTree.InsertNode(values[i]);
             }
    }

    BinaryTree binaryTree;
   
};


class TreeAxioms : public ::testing::Test
{
protected:
    
        virtual void SetUp() {
        int values[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

        for(int i = 0; i < 12; ++i) {
            binaryTree.InsertNode(values[i]);
             }
    } 

    BinaryTree binaryTree;
   
};


TEST_F(EmptyTree, InsertDelete){

    EXPECT_TRUE(binaryTree.GetRoot() == NULL);
    EXPECT_TRUE(binaryTree.InsertNode(2).first);
    EXPECT_TRUE(binaryTree.FindNode(2) != NULL);
    EXPECT_TRUE(binaryTree.GetRoot() != NULL);
   
    EXPECT_TRUE(binaryTree.InsertNode(3).first);

    //duplicitna hodnota 
    EXPECT_FALSE(binaryTree.InsertNode(2).first);

    EXPECT_TRUE(binaryTree.DeleteNode(2));
    EXPECT_FALSE(binaryTree.FindNode(2) != NULL);

}


TEST_F(EmptyTree, StructureTest){

    EXPECT_TRUE(binaryTree.GetRoot() == NULL);

    std::pair<bool, BinaryTree::Node_t *> member1 = binaryTree.InsertNode(1);
    EXPECT_TRUE(member1.first);
    BinaryTree::Node_t * node1 = member1.second;
    EXPECT_TRUE(node1->key == 1);
    EXPECT_TRUE(node1->color == BinaryTree::BLACK);
    EXPECT_TRUE(node1->pParent == NULL);
    EXPECT_TRUE(node1->pRight != NULL);
    EXPECT_TRUE(node1->pLeft != NULL);


    std::pair<bool, BinaryTree::Node_t *> member2 = binaryTree.InsertNode(2);
    EXPECT_TRUE(member2.first);
    BinaryTree::Node_t * node2 = member2.second;
    ASSERT_TRUE(node2->pParent != NULL);
    EXPECT_TRUE(node2->pParent->key == 1);
    EXPECT_TRUE(node2->pRight != NULL);
    EXPECT_TRUE(node2->pLeft != NULL);

    ASSERT_TRUE(node1->pRight != NULL);
    EXPECT_TRUE(node1->pRight->key == 2);


    std::pair<bool, BinaryTree::Node_t *> member3 = binaryTree.InsertNode(3);
    EXPECT_TRUE(member3.first);
    BinaryTree::Node_t * node3 = member3.second;
    ASSERT_TRUE(node3->pParent != NULL);
    EXPECT_TRUE(node3->pParent->key == 2);
    EXPECT_TRUE(node3->pRight != NULL);
    EXPECT_TRUE(node3->pLeft != NULL);

    ASSERT_TRUE(node2->pRight->key == 3); 
    ASSERT_TRUE(node2->pLeft->key == 1); 
}




TEST_F(NonEmptyTree, InsertDelete){

       
    EXPECT_TRUE(binaryTree.GetRoot() != NULL);
    EXPECT_TRUE(binaryTree.InsertNode(13).first);

    EXPECT_TRUE(binaryTree.FindNode(2) != NULL);
    EXPECT_FALSE(binaryTree.InsertNode(2).first);

    EXPECT_TRUE(binaryTree.DeleteNode(13));
    EXPECT_FALSE(binaryTree.FindNode(13) != NULL);

    int values[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

        for(int i = 0; i < 12; ++i) {
            binaryTree.DeleteNode(values[i]);
             }

    EXPECT_TRUE(binaryTree.GetRoot() == NULL); 
}


TEST_F(TreeAxioms, Axiom1){
    
   
	std::vector<BinaryTree::Node_t *> leafs;
	binaryTree.GetLeafNodes(leafs);

    int leafsSize = leafs.size();
	for(int i = 0; i < leafsSize; ++i){
		EXPECT_TRUE(BinaryTree::BLACK == leafs[i]->color);
	}
}

TEST_F(TreeAxioms, Axiom2){
  
	std::vector<BinaryTree::Node_t *> leafs;
    binaryTree.GetAllNodes(leafs);

    int leafsSize = leafs.size();
	for(int i = 0; i < leafsSize; ++i){
		
        if(leafs[i]->color == BinaryTree::RED){

            if(leafs[i]-> pRight != NULL) {
                EXPECT_EQ(leafs[i]->pRight->color, BinaryTree::BLACK);
            }

            if(leafs[i]-> pLeft != NULL) {
                EXPECT_EQ(leafs[i]->pLeft->color, BinaryTree::BLACK);
            }
        }

	}

}


TEST_F(TreeAxioms, Axiom3){
	
    std::vector<BinaryTree::Node_t *> leafs;
	binaryTree.GetLeafNodes(leafs);


    int counter = 0;
    int comparison;
    int leafsSize = leafs.size();
	for(int i = 0; i < leafsSize; ++i){

        BinaryTree::Node_t * node = leafs[i] -> pParent;
        while(node != NULL) {
            if(node->color == BinaryTree::Color_t::BLACK){
                counter++;
            }
            node = node -> pParent;
        }
    if(i >= 1) {
        ASSERT_EQ(comparison, counter);
    }
    comparison = counter;
    counter = 0;
    
    }


}


//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy Red-Black Tree, testujte nasledujici:
// 1. Verejne rozhrani stromu
//    - InsertNode/DeleteNode a FindNode
//    - Chovani techto metod testuje pro prazdny i neprazdny strom.
// 2. Axiomy (tedy vzdy platne vlastnosti) Red-Black Tree:
//    - Vsechny listove uzly stromu jsou *VZDY* cerne.
//    - Kazdy cerveny uzel muze mit *POUZE* cerne potomky.
//    - Vsechny cesty od kazdeho listoveho uzlu ke koreni stromu obsahuji
//      *STEJNY* pocet cernych uzlu.
//============================================================================//

/*** Konec souboru black_box_tests.cpp ***/
