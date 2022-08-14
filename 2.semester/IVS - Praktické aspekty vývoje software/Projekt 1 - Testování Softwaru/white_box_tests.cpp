//======== Copyright (c) 2017, FIT VUT Brno, All rights reserved. ============//
//
// Purpose:     White Box - Tests suite
//
// $NoKeywords: $ivs_project_1 $white_box_code.cpp
// $Author:     Vanessa Jóriová <xjorio00@stud.fit.vutbr.cz>
// $Date:       $2020-03-04
//============================================================================//
/**
 * @file white_box_tests.cpp
 * @author Vanessa Jóriová
 * 
 * @brief Implementace testu prace s maticemi.
 */

#include "gtest/gtest.h"
#include "white_box_code.h"

//============================================================================//
// ** ZDE DOPLNTE TESTY **
//
// Zde doplnte testy operaci nad maticemi. Cilem testovani je:
// 1. Dosahnout maximalniho pokryti kodu (white_box_code.cpp) testy.
// 2. Overit spravne chovani operaci nad maticemi v zavislosti na rozmerech 
//    matic.
//============================================================================//

class MatrixTest : public ::testing::Test {
protected:
	
    Matrix set4x4Matrix(){

        Matrix matrix(4,4);
        matrix.set(std::vector<std::vector<double>> {
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 16},
                });
        return matrix;

    };


     Matrix setAnother4x4Matrix(){

        Matrix matrix(4,4);
        matrix.set(std::vector<std::vector<double>> {
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 18},
                });
        return matrix;

    };



     Matrix set4x2Matrix(){

        Matrix matrix(4,2);
        matrix.set(std::vector<std::vector<double>> {
				{1, 2},
				{3, 4},
                {5, 6},
                {7, 8},
                });
        return matrix;


    };

    Matrix set3x3Matrix(){

        Matrix matrix(3,3);
        matrix.set(std::vector<std::vector<double>> {
				{1, 2, 3},
				{4, 5, 6},
                {7, 8, 9},
                });

        return matrix;


    };


	};


TEST_F(MatrixTest, Constructor) {
  
    //spravne zadane rozmery matice 
    EXPECT_NO_THROW(Matrix());
    EXPECT_NO_THROW(Matrix(1,1));
    EXPECT_NO_THROW(Matrix(5,6));
    
    //nespravne zadane rozmery matice
    EXPECT_ANY_THROW(Matrix(0,2));
    EXPECT_ANY_THROW(Matrix(-2,1));
}


TEST_F(MatrixTest, SetMatrix) {
    Matrix matrix(1,1);
    Matrix matrix2(1,1);
    Matrix matrix3(2,2);
    
    //manualne zadanie hodnot pre dve 1x1 matice
    EXPECT_TRUE(matrix.set(0,0,5));
    EXPECT_TRUE(matrix2.set (0,0,5));

    EXPECT_EQ(matrix, matrix2);
    EXPECT_EQ(5, matrix.get(0,0));

    //manualne zadanie hodnot pre 2x2 maticu
    EXPECT_TRUE(matrix3.set(0,0,5));
    EXPECT_EQ(5, matrix3.get(0,0));
    EXPECT_TRUE(matrix3.set(0,1,6));
    EXPECT_EQ(6, matrix3.get(0,1));
    EXPECT_TRUE(matrix3.set(1,0,7));
    EXPECT_EQ(7, matrix3.get(1,0));
    EXPECT_TRUE(matrix3.set(1,1,8));
    EXPECT_EQ(8, matrix3.get(1,1));
    
    //zadanie hodnot pre neexistujuci index
    EXPECT_FALSE(matrix3.set(2,0,9));
    EXPECT_FALSE(matrix.set(8,9, 5));
    EXPECT_ANY_THROW(matrix.get(4,5));
}

TEST_F(MatrixTest, SetMatrixVector) {
   Matrix matrix(2,3);
   
    EXPECT_TRUE(matrix.set(std::vector<std::vector<double>> {
			{5,-8, 16},
            {-7, 9.1, 2}	
		}));
     
    EXPECT_EQ(-8, matrix.get(0,1));

    //skalarne zadanie tych istych hodnot
    Matrix matrix2 (2,3);
    matrix2.set(0,0,5);
    matrix2.set(0,1,-8);
    matrix2.set(0,2,16);
    matrix2.set(1,0,-7);
    matrix2.set(1,1,9.1);
    matrix2.set(1,2,2);

    EXPECT_TRUE(matrix == matrix2);

    
    //zadanie nespravnych hodnot vzhladom na velkost matice
    Matrix matrix3(1,2);
    EXPECT_FALSE(matrix3.set(std::vector<std::vector<double>> {
			{5,8, 16},
            {7, 9, 2}	
		}));
}

TEST_F(MatrixTest, Plus) {
  
    //scitanie rovnakych matic
    EXPECT_NO_THROW(set4x4Matrix() + set4x4Matrix());

    //scitanie rovnako velkych matic s roznymi hodnotami
    EXPECT_NO_THROW(set4x4Matrix() + setAnother4x4Matrix());


    //scitanie matic s rozdielnymi rozmermi
    EXPECT_ANY_THROW(set4x4Matrix() + set3x3Matrix());
    EXPECT_ANY_THROW(set4x2Matrix() + set4x4Matrix());
    

    Matrix result = set4x4Matrix() + set4x4Matrix();

    Matrix expected(4,4);
    expected.set(std::vector<std::vector<double>> {
				{2, 4, 6, 8},
				{10, 12, 14, 16},
				{18, 20, 22, 24},
				{26, 28, 30, 32},
                });

    EXPECT_EQ(result, expected);

}


TEST_F(MatrixTest, Equal){
    //rovnaka matica
    EXPECT_TRUE(set4x4Matrix() == set4x4Matrix());
    
    //rozdielne rozmery
    EXPECT_ANY_THROW(set4x4Matrix() == set4x2Matrix());
    
    //rozdielne hodnoty
    EXPECT_FALSE(set4x4Matrix() == setAnother4x4Matrix());
}

TEST_F(MatrixTest, Multiply) {
    //nasobenie rovnako velkych matic
    EXPECT_NO_THROW(set4x4Matrix() * setAnother4x4Matrix());

    //nasobenie pripustne rozdielnych matic
    EXPECT_NO_THROW(set4x4Matrix() * set4x2Matrix());

    //nasobenie nepripustne rozdielnych matic
    EXPECT_ANY_THROW(set4x4Matrix() * set3x3Matrix());
    
    Matrix result = set4x4Matrix() * set4x4Matrix();

     Matrix expected(4,4);
     expected.set(std::vector<std::vector<double>> {
				{90, 100, 110, 120},
				{202, 228, 254, 280},
				{314, 356, 398, 440},
				{426, 484, 542, 600},
                });

    EXPECT_EQ(result, expected); 

    //nasobenie skalarom 
    Matrix result2 = set4x4Matrix() * 2;

    Matrix expected2(4,4);
    expected2.set(std::vector<std::vector<double>> {
				{2, 4, 6, 8},
				{10, 12, 14, 16},
				{18, 20, 22, 24},
				{26, 28, 30, 32},
                });

    EXPECT_EQ(result2, expected2);

   
    EXPECT_EQ(2, result2.get(0,0)); 
    EXPECT_EQ(4, result2.get(0,1)); 
}


TEST_F(MatrixTest, Equation){

    Matrix matrix1x1(1,1);
    matrix1x1.set(std::vector<std::vector<double>> {
				{1}
                });


    Matrix singular(2,2);
    singular.set(std::vector<std::vector<double>> {
				{1, 1},
				{1, 1},
                });



    Matrix matrix(2,2);
    matrix.set(std::vector<std::vector<double>> {
				{2, 1},
				{2, 2},
                });

   Matrix matrix3x3Sing(3,3);
    matrix3x3Sing.set(std::vector<std::vector<double>> {
				{1, 1, 1},
				{2, 2, 2},
                {3, 3, 3},
                });

    Matrix matrix3x3(3,3);
    matrix3x3.set(std::vector<std::vector<double>> {
				{2, 1, -1},
				{3, 2, 2},
                {4, -2, 3},
                });


    Matrix notSquare(4,2);
    notSquare.set(std::vector<std::vector<double>> {
				{1, 1},
				{7, -9},
                {1, 1044},
                {8, 1044},
                });

     Matrix AnotherNotSquare(1,5);
     AnotherNotSquare.set(std::vector<std::vector<double>> {
				{2, 3, 4, 5, 6},
                });

    Matrix matrix4x4(4,4);
        matrix4x4.set(std::vector<std::vector<double>> {
				{1, 8, 14, 5},
				{3, 6, 4, 7},
				{2, 2, 2, 3},
				{8, 2, 3, 1},
                });

    

   //nespravny pocet hodnot na pravej strane 
   EXPECT_ANY_THROW(matrix.solveEquation(std::vector<double> {0}));
   EXPECT_ANY_THROW(matrix.solveEquation(std::vector<double> {0, 0, 0}));

    //singularna matica
    EXPECT_ANY_THROW(singular.solveEquation(std::vector<double> {0, 0}));
    EXPECT_ANY_THROW(matrix3x3Sing.solveEquation(std::vector<double> {3, 6, 9}));

    
    //nestvorcova matica
    EXPECT_ANY_THROW(notSquare.solveEquation(std::vector<double> {1, 7, 0, 10}));
    EXPECT_ANY_THROW(AnotherNotSquare.solveEquation(std::vector<double> {1}));
   
    //spravne hodnoty 
    std::vector<double> result;
    
    EXPECT_NO_THROW(result = matrix.solveEquation(std::vector<double> {5, 6}));
    std::vector<double> expected = {2,1};
    EXPECT_EQ(result, expected);


    EXPECT_NO_THROW(result = matrix3x3.solveEquation(std::vector<double> {1, 13, 9}));
    expected = {1,2, 3};
    EXPECT_EQ(result, expected);


   EXPECT_NO_THROW(result = matrix1x1.solveEquation(std::vector<double> {5}));
    expected = {5};
    EXPECT_EQ(result, expected);


    EXPECT_NO_THROW(result = matrix4x4.solveEquation(std::vector<double> {79, 55, 24, 25}));
    expected = {1, 2, 3, 4};
    EXPECT_EQ(result, expected);


}


