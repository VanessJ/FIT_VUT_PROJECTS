##
# @file math_lib.py
# @brief Library used for our calculator
# @author Marián Zimmermann
# @author Vanessa Jórijová
# @date April 2020
#
##

import math
##
# @brief constant PI used during tests.
PI = math.pi


##
# @brief Negation of a number.
# @param x Number which will be negated.
# @return Negated value of the number.
#
def neg(x):
    return (x * -1)

##
# @brief Addition of 2 numbers.
# @param x Addend.
# @param y Addend.
# @return Sum of the addends rounded to 5 decimals.
#
def add(x, y):
    return round(x + y, 5)


##
# @brief Subtraction of 2 numbers.
# @param x Minuend.
# @param y Subtrahend.
# @return Difference of Minuend and Subtrahend rounded to 5 decimals.
#
def sub(x, y):
    return round(x - y, 5)
##
# @brief Multiplication of 2 numbers.
# @param x Multiplier.
# @param y Multiplicand.
# @return Product of multiplier and multiplicand rounded to 5 decimals.
#


def mul(x, y):
    return round(x * y, 5)


##
# @brief Division of 2 numbers.
# @param x Dividend.
# @param y Divisor.
# @return Quotient of dividend and divisor number rounded to 5 decimals.
# @exception ZeroDivisionError if "y"==0.
#
def div(x, y):
    try:
        return round(x / y, 5)
    except ZeroDivisionError as e:
        raise e


##
# @brief power of a number.
# @param x Cardinal number.
# @param y Exponent.
# @return Cardinal number powered by exponent rounded to 5 decimals.
# @exception Value error if exponent is not natural number.
#
def pow(x,y):

    if y<0 or isinstance(y, float):
        raise ValueError
    return round ((x ** y), 5)


##
# @brief  Root of a number.
# @param x Number which will be rooted.
# @param y Value of the root.
# @return yth root value of the number rounded to 10 decimals.
# @exception Value error if rooted number is smaller than zero and root is even.
# @exception Value error if root is not natural number.
def root(x,y):
    if x<0 and (y%2 ==0):
        raise ValueError
    if y<=0 or isinstance(y, float):
        raise ValueError
    return round((math.copysign(1,x) * abs(x) ** (y**-1)), 5)


##
# @brief Factorial of a number.
# @param x Number which will be factorized
# @return Factorized value of the number rounded to 5 decimals
# @exception ValueError if "x" is decimal
# @exception ValueError if "x"<0
#
def factorial(x):
    try:
        return round(math.factorial(x), 5)
    except ValueError as e:
        raise e


##
# @brief Sinus value of a number.
# @param x Number in radians from which will be the sinus calculated.
# @return Sinus value of the number rounded to 5 decimals.
#
def sinus(x):
    return round(math.sin(x), 5)


##
# @brief Cosine value of a number.
# @param x Number in radians from which will be the Cosine calculated.
# @return Sinus value of the number rounded to 5 decimals.
#
def cosine(x):
    return round(math.cos(x), 5)

