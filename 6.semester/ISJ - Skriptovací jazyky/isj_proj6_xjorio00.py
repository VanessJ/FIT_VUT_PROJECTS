#!/usr/bin/env python3

class Polynomial:
    def __init__(self, *args, **kwargs):
        """

        @brief Constructs instance of polynomial. Polynomial is internally represented as dictionary consisting of
                degree:value pairs - degree of coefficients and their value. Can be initialized by passing values of
                degrees in form of list or integers (first value is coefficient 0, second coefficient 1 etc.) or by
                passing named parameters in form x{degree}:value (x1 = 0 etc.).
        :param args: List of integer values or integer values representing value of coefficients starting by coefficient 0
        :param kwargs: Named parameters in form x{coefficient} = value
        """
        self.coefficients_and_values = {}
        if args:
            if isinstance(args[0], list):
                coefficients = args[0]
            else:
                coefficients = list(args)

            for degree, value in enumerate(coefficients):
                value = coefficients[degree]
                if value != 0:
                    self.coefficients_and_values.update({degree: value})
        elif kwargs:
            for degree, value in kwargs.items():
                if value != 0:
                    degree = int(degree[1:])
                    self.coefficients_and_values.update({degree: value})
        else:
            self.coefficients_and_values = {0: 0}

        self.coefficients_and_values = dict(sorted(self.coefficients_and_values.items(), reverse=True))

    def __str__(self):
        """

        @brief: String representation of polynomial in common form - starting by biggest coefficient and followed by
                other coefficients in descending order
        :return: String representation of polynomial
        """
        polynomial_string = ""

        for degree, value in self.coefficients_and_values.items():
            if value == 0 and degree != 0:
                continue

            if value > 0:
                sign = " + "
            else:
                sign = " - "
            value = abs(value)

            if degree == 0:
                polynomial_string = polynomial_string + sign + str(value)
                break

            if value < 2:
                value = ""

            polynomial_string = polynomial_string + sign + str(value)
            if degree != 0:
                polynomial_string = polynomial_string + "x"
            if degree > 1:
                polynomial_string = polynomial_string + "^" + str(degree)
        polynomial_string = polynomial_string.strip(" +-")

        if polynomial_string == "":
            polynomial_string = "0"

        return polynomial_string

    def __eq__(self, other):
        """

        @brief: Comparison of polynomial based on coefficients and their values
        :param other: Other polynomial
        :return: True if polynomials are equal, false if not
        """
        return self.coefficients_and_values == other.coefficients_and_values

    def __add__(self, other):
        """

        @brief: Sums two polynomial instances
        :param other: Polynomial instance
        :return: Sum of two polynomials in form of polynomial instance
        """
        polynomial_sum = {}
        self_max_degree = max(self.coefficients_and_values.keys())
        other_max_degree = max(other.coefficients_and_values.keys())
        if self_max_degree >= other_max_degree:
            max_degree = self_max_degree
        else:
            max_degree = other_max_degree
        for degree in reversed(range(0, max_degree + 1)):
            first_value = None
            second_value = None

            if degree in self.coefficients_and_values:
                first_value = self.coefficients_and_values[degree]
            if degree in other.coefficients_and_values:
                second_value = other.coefficients_and_values[degree]
            if first_value is None and second_value is None:
                continue
            elif first_value is None:
                polynomial_sum.update({f'x{degree}': second_value})
            elif second_value is None:
                polynomial_sum.update({f'x{degree}': first_value})
            else:
                polynomial_sum.update({f'x{degree}': first_value + second_value})
        return Polynomial(**polynomial_sum)

    def __pow__(self, power):
        """

        @brief Calculates polynomial of given power
        :param power: Power (zero or positive integer)
        :return: Result in form of polynomial instance
        """
        if power > 0:
            polynomial_pow_results = self.coefficients_and_values

            for i in range(power - 1):
                temp = {}

                for degree, value in self.coefficients_and_values.items():
                    for degree2, value2 in polynomial_pow_results.items():

                        if degree + degree2 in temp:
                            temp[degree + degree2] = temp[degree + degree2] + value * value2
                        else:
                            temp[degree + degree2] = value * value2
                polynomial_pow_results = temp

            final_polynomial = {}
            for degree, value in polynomial_pow_results.items():
                final_polynomial.update({f'x{degree}': value})
            return Polynomial(**final_polynomial)
        else:
            return Polynomial(**{0: 1})


    def derivative(self):
        """

        @brief: Calculates first derivative of polynomial instance
        :return: Derivative of polynomial in form of polynomial instance
        """
        poly_dict = {}
        for degree, value in self.coefficients_and_values.items():
            if degree > 0:
                poly_dict.update({f'x{degree - 1}': (degree * value)})
        if not poly_dict:
            poly_dict.update({"x0": 0})

        return Polynomial(**poly_dict)

    def at_value(self, first, second=None):
        """

        @brief: Calculates value of specific x of polynomial. Two values can be entered, in this case the result will be
                difference between second and first value
        :param first: First x value as integer
        :param second: Second x value as integer
        :return: result As integer
        """
        if second:
            return self.at_value(second) - self.at_value(first)

        poly_sum = 0
        for degree, value in self.coefficients_and_values.items():
            if degree == 0:
                poly_sum += value
            else:
                poly_sum += value * first ** degree
        return poly_sum


def test():
    assert str(Polynomial(0, 1, 0, -1, 4, -2, 0, 1, 3, 0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5, 1, 0, -1, 4, -2, 0, 1, 3, 0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3=-1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2, 0, 3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1) + Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1, 1, 1, 0]) + Polynomial(1, -1, 1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(pol1 + pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1, x1=1) ** 1) == "x - 1"
    assert str(Polynomial(x0=-1, x1=1) ** 2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1, x1=1)
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3 ** 4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2, x1=3, x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2, x1=3, x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2, 3, 4, -5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5) == 44
    pol5 = Polynomial([1, 0, -2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1, 3.6) == -23.92
    assert pol5.at_value(-1, 3.6) == -23.92


if __name__ == "__main__":
    test()
