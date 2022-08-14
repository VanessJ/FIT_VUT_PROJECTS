##
# @file math_lib_test.py
# @brief TDD tests for our library
# @author Marián Zimmermann
# @author Vanessa Jóriová
# @date April 2020
import pytest
import math_lib

def test_neg_possitive():
    assert math_lib.neg(0) == 0
    assert math_lib.neg(1) == -1
    assert math_lib.neg(100) == -100
    assert math_lib.neg(1.745) == -1.745


def test_neg_negative():
    assert math_lib.neg(-1) == 1
    assert math_lib.neg(-100) == 100
    assert math_lib.neg(-1.745) == 1.745


def test_add_positive():
    assert math_lib.add(1, 1) == 2
    assert math_lib.add(1, 4) == 5
    assert math_lib.add(0, 0) == 0
    assert math_lib.add(9, 10) == 19
    assert math_lib.add(7, 8) == 15
    assert math_lib.add(30, 30) == 60
    assert math_lib.add(40, 45) == 85
    assert math_lib.add(100, 260) == 360
    assert math_lib.add(1050, 1020) == 2070
    assert math_lib.add(0.3, 0.3) == 0.6
    assert math_lib.add(0.467, 2.253) == 2.72
    assert math_lib.add(0.333333, 0.3333333) == 0.66667
    assert math_lib.add(0.222222, 0.222222) == 0.44444


def test_add_negative():
    assert math_lib.add(-1, -1) == -2
    assert math_lib.add(-1, -5) == -6
    assert math_lib.add(-7, -8) == -15
    assert math_lib.add(-4, -10) == -14
    assert math_lib.add(-3, -8) == -11
    assert math_lib.add(-30, -30) == -60
    assert math_lib.add(-40, -45) == -85
    assert math_lib.add(-100, -260) == -360
    assert math_lib.add(-1050, -1020) == -2070
    assert math_lib.add(-0.3, -0.3) == -0.6
    assert math_lib.add(-0.467, -2.253) == -2.72
    assert math_lib.add(-0.333333, -0.3333333) == -0.66667
    assert math_lib.add(-0.222222, -0.222222) == -0.44444


def test_add_mixed():
    assert math_lib.add(1, -1) == 0
    assert math_lib.add(-1, 5) == 4
    assert math_lib.add(-7, 8) == 1
    assert math_lib.add(4, -10) == -6
    assert math_lib.add(3, -8) == -5
    assert math_lib.add(-30, 30) == 0
    assert math_lib.add(-40, 45) == 5
    assert math_lib.add(-100, 260) == 160
    assert math_lib.add(-1050, 1020) == -30
    assert math_lib.add(-0.3, 0.3) == 0
    assert math_lib.add(-0.467, 2.253) == 1.786
    assert math_lib.add(0.467, -2.253) == -1.786
    assert math_lib.add(-0.333332, 0.3333333) == 0
    assert math_lib.add(-0.222222, 0.222228) == 0.00001


def test_sub_positive():
    assert math_lib.sub(1, 1) == 0
    assert math_lib.sub(6, 7) == -1
    assert math_lib.sub(0, 4) == -4
    assert math_lib.sub(10, 21) == -11
    assert math_lib.sub(20, 3) == 17
    assert math_lib.sub(40, 80) == -40
    assert math_lib.sub(1, 99) == -98
    assert math_lib.sub(1000, 463) == 537
    assert math_lib.sub(2000, 4000) == -2000
    assert math_lib.sub(0.5, 0.5) == 0
    assert math_lib.sub(2.456, 0.123) == 2.333
    assert math_lib.sub(0.123, 2.456) == -2.333
    assert math_lib.sub(0.666666, 0.333333) == 0.33333
    assert math_lib.sub(0.333333, 0.666666) == -0.33333
    assert math_lib.sub(0.666667, 0.333331) == 0.33334
    assert math_lib.sub(0.333331, 0.666667) == -0.33334


def test_sub_negative():
    assert math_lib.sub(-1, -1) == 0
    assert math_lib.sub(-6, -7) == 1
    assert math_lib.sub(0, -4) == 4
    assert math_lib.sub(-10, -21) == 11
    assert math_lib.sub(-20, -3) == -17
    assert math_lib.sub(-40, -80) == 40
    assert math_lib.sub(-1, -99) == 98
    assert math_lib.sub(-1000, -463) == -537
    assert math_lib.sub(-2000, -4000) == 2000
    assert math_lib.sub(-2.456, -0.123) == -2.333
    assert math_lib.sub(-0.123, -2.456) == 2.333
    assert math_lib.sub(-0.5, -0.5) == 0
    assert math_lib.sub(-0.666666, -0.333333) == -0.33333
    assert math_lib.sub(-0.333333, -0.666666) == 0.33333
    assert math_lib.sub(-0.666667, -0.333331) == -0.33334
    assert math_lib.sub(-0.333331, -0.666667) == 0.33334


def test_sub_mixed():
    assert math_lib.sub(-1, 1) == -2
    assert math_lib.sub(6, -7) == 13
    assert math_lib.sub(0, 4) == -4
    assert math_lib.sub(-10, 21) == -31
    assert math_lib.sub(-20, 3) == -23
    assert math_lib.sub(40, -80) == 120
    assert math_lib.sub(-1, 99) == -100
    assert math_lib.sub(1000, -463) == 1463
    assert math_lib.sub(-2000, 4000) == -6000
    assert math_lib.sub(0.5, -0.5) == 1
    assert math_lib.sub(2.456, -0.123) == 2.579
    assert math_lib.sub(-0.123, 2.456) == -2.579
    assert math_lib.sub(0.555555, -0.333333) == 0.88889
    assert math_lib.sub(-0.333333, 0.555555) == -0.88889
    assert math_lib.sub(-0.555553, 0.333332) == -0.88888
    assert math_lib.sub(0.333332, -0.555553) == 0.88888


def test_mul_postive():
    assert math_lib.mul(1, 4) == 4
    assert math_lib.mul(2, 8) == 16
    assert math_lib.mul(11, 3) == 33
    assert math_lib.mul(18, 4) == 72
    assert math_lib.mul(23, 8) == 184
    assert math_lib.mul(66, 6) == 396
    assert math_lib.mul(100, 4) == 400
    assert math_lib.mul(1002, 6) == 6012
    assert math_lib.mul(980, 40) == 39200
    assert math_lib.mul(1.5, 4.2) == 6.3
    assert math_lib.mul(2.5, 8) == 20
    assert math_lib.mul(0.465, 0) == 0
    assert math_lib.mul(0.789, 0.654) == 0.51601
    assert math_lib.mul(0.234, 0.658) == 0.15397


def test_mul_negative():
    assert math_lib.mul(-1, -4) == 4
    assert math_lib.mul(-2, -8) == 16
    assert math_lib.mul(-11, -3) == 33
    assert math_lib.mul(-18, -4) == 72
    assert math_lib.mul(-23, -8) == 184
    assert math_lib.mul(-66, -6) == 396
    assert math_lib.mul(-100, -4) == 400
    assert math_lib.mul(-1002, -6) == 6012
    assert math_lib.mul(-980, -40) == 39200
    assert math_lib.mul(-1.5, -4.2) == 6.3
    assert math_lib.mul(-2.5, -8) == 20
    assert math_lib.mul(-0.465, 0) == 0
    assert math_lib.mul(-0.789, -0.654) == 0.51601
    assert math_lib.mul(-0.234, -0.658) == 0.15397


def test_mul_mixed():
    assert math_lib.mul(-1, 4) == -4
    assert math_lib.mul(2, -8) == -16
    assert math_lib.mul(-11, 3) == -33
    assert math_lib.mul(18, -4) == -72
    assert math_lib.mul(-23, 8) == -184
    assert math_lib.mul(66, -6) == -396
    assert math_lib.mul(-100, 4) == -400
    assert math_lib.mul(1002, -6) == -6012
    assert math_lib.mul(-980, 40) == -39200
    assert math_lib.mul(-1.5, 4.2) == -6.3
    assert math_lib.mul(-2.5, 8) == -20
    assert math_lib.mul(-0.465, 0) == 0
    assert math_lib.mul(-0.789, 0.654) == -0.51601
    assert math_lib.mul(-0.234, 0.658) == -0.15397


def test_div_postive():
    assert math_lib.div(1, 1) == 1
    assert math_lib.div(10, 5) == 2
    assert math_lib.div(56, 8) == 7
    assert math_lib.div(81, 9) == 9
    assert math_lib.div(98, 7) == 14
    assert math_lib.div(240, 16) == 15
    assert math_lib.div(979, 11) == 89
    assert math_lib.div(3360, 8) == 420
    assert math_lib.div(20944, 112) == 187
    assert math_lib.div(2, 1.5) == 1.33333
    assert math_lib.div(11, 2.2) == 5
    assert math_lib.div(0.5, 0.8) == 0.625
    assert math_lib.div(0.4, 0.04) == 10
    assert math_lib.div(100, 6) == 16.66667


def test_div_negative():
    assert math_lib.div(-1, -1) == 1
    assert math_lib.div(-10, -5) == 2
    assert math_lib.div(-56, -8) == 7
    assert math_lib.div(-81, -9) == 9
    assert math_lib.div(-98, -7) == 14
    assert math_lib.div(-240, -16) == 15
    assert math_lib.div(-979, -11) == 89
    assert math_lib.div(-3360, -8) == 420
    assert math_lib.div(-20944, -112) == 187
    assert math_lib.div(-2, -1.5) == 1.33333
    assert math_lib.div(-11, -2.2) == 5
    assert math_lib.div(-0.5, -0.8) == 0.625
    assert math_lib.div(-0.4, -0.04) == 10
    assert math_lib.div(-100, -6) == 16.66667


def test_div_mixed():
    assert math_lib.div(-1, 1) == -1
    assert math_lib.div(10, -5) == -2
    assert math_lib.div(-56, 8) == -7
    assert math_lib.div(81, -9) == -9
    assert math_lib.div(-98, 7) == -14
    assert math_lib.div(240, -16) == -15
    assert math_lib.div(-979, 11) == -89
    assert math_lib.div(3360, -8) == -420
    assert math_lib.div(-20944, 112) == -187
    assert math_lib.div(-2, 1.5) == -1.33333
    assert math_lib.div(-11, 2.2) == -5
    assert math_lib.div(-0.5, 0.8) == -0.625
    assert math_lib.div(-0.4, 0.04) == -10
    assert math_lib.div(-100, 6) == -16.66667


def test_div_error():
    with pytest.raises(ZeroDivisionError):
        math_lib.div(10, 0)
    with pytest.raises(ZeroDivisionError):
        math_lib.div(-114, 0)
    with pytest.raises(ZeroDivisionError):
        math_lib.div(107085, 0)
    with pytest.raises(ZeroDivisionError):
        math_lib.div(0.7, 0)

def test_pow_positive():
    assert math_lib.pow(2,2) == 4
    assert math_lib.pow(61, 2) == 3721
    assert math_lib.pow(1058, 2) == 1119364
    assert math_lib.pow(4, 4) == 256
    assert math_lib.pow(5, 6) == 15625
    assert math_lib.pow(18, 5) == 1889568
    assert math_lib.pow(4, 7) == 16384
    assert math_lib.pow(7, 9) == 40353607
    assert math_lib.pow(4.2, 3) == 74.088
    assert math_lib.pow(1.8, 5) == 18.89568
    assert math_lib.pow(2.24, 6) == 126.32465



def test_pow_error():
    with pytest.raises(ValueError):
        math_lib.pow(2, -2)
    with pytest.raises(ValueError):
        math_lib.pow(8, -11)
    with pytest.raises(ValueError):
        math_lib.pow(0.3, 0.2)
    with pytest.raises(ValueError):
        math_lib.pow(7, 1.1)




def test_root():
    assert math_lib.root(4, 2) == 2
    assert math_lib.root(8, 3) == 2
    assert math_lib.root(-8, 3) == -2
    assert math_lib.root(4.84, 2) == 2.2
    assert math_lib.root(0.3, 2) == 0.54772
    assert math_lib.root(0.027, 3) == 0.3
    assert math_lib.root(-0.027, 3) == -0.3     
    assert math_lib.root(512, 3) == 8 
    assert math_lib.root(-512, 3) == -8 
    assert math_lib.root(2025, 2) == 45
    assert math_lib.root(2476099, 5) == 19
    assert math_lib.root(-2476099, 5) == -19
    assert math_lib.root(2401, 4) == 7


def test_root_error():
    with pytest.raises(ValueError):
        math_lib.root(-4, 2)
    with pytest.raises(ValueError):
        math_lib.root(-4.84, 2)
    with pytest.raises(ValueError):
        math_lib.root(-2401, 4)
    with pytest.raises(ValueError):
        math_lib.root(0.3, 0.2)
    with pytest.raises(ValueError):
        math_lib.root(-512, 1.3)





def test_factorial():
    assert math_lib.factorial(0) == 1
    assert math_lib.factorial(1) == 1
    assert math_lib.factorial(120)
    assert math_lib.factorial(10) == 3628800


def test_factorial_error():
    with pytest.raises(ValueError):
        math_lib.factorial(-1)
    with pytest.raises(ValueError):
        math_lib.factorial(-5)
    with pytest.raises(ValueError):
        math_lib.factorial(-0.5)
    with pytest.raises(ValueError):
        math_lib.factorial(0.5)


def test_sinus_positive():
    assert math_lib.sinus(0) == 0
    assert math_lib.sinus(math_lib.PI / 6) == 0.5
    assert math_lib.sinus(math_lib.PI / 4) == 0.70711
    assert math_lib.sinus(math_lib.PI / 3) == 0.86603
    assert math_lib.sinus(math_lib.PI / 2) == 1
    assert math_lib.sinus(math_lib.PI) == 0


def test_sinus_negative():
    assert math_lib.sinus(math_lib.PI / -6) == -0.5
    assert math_lib.sinus(math_lib.PI / -4) == -0.70711
    assert math_lib.sinus(math_lib.PI / -3) == -0.86603
    assert math_lib.sinus(math_lib.PI / -2) == -1
    assert math_lib.sinus(-math_lib.PI) == 0


def test_cosine_positive():
    assert math_lib.cosine(0) == 1
    assert math_lib.cosine(math_lib.PI / 6) == 0.86603
    assert math_lib.cosine(math_lib.PI / 4) == 0.70711
    assert math_lib.cosine(math_lib.PI / 3) == 0.5
    assert math_lib.cosine(math_lib.PI / 2) == 0
    assert math_lib.cosine(math_lib.PI) == -1


def test_cosine_negative():
    assert math_lib.cosine(math_lib.PI / -6) == 0.86603
    assert math_lib.cosine(math_lib.PI / -4) == 0.70711
    assert math_lib.cosine(math_lib.PI / -3) == 0.5
    assert math_lib.cosine(math_lib.PI / -2) == 0
    assert math_lib.cosine(-math_lib.PI) == -1
 
