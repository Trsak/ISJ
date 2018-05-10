#!/usr/bin/env python3


class Polynomial:
    """
    Polynomial class that represents polynomial and implements it's operations and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Instance of Polynomial, polynomials can be represented as one list, arguments or keyword arguments.
        """
        self.polynomials = {}

        if len(args) == 1 and isinstance(args[0], list):  # Polynomials represented as list
            index = 0
            for polynomial in args[0]:
                self.polynomials[index] = polynomial
                index += 1
        elif len(args) > 0:  # Polynomials represented as arguments
            index = 0
            for polynomial in args:
                self.polynomials[index] = polynomial
                index += 1
        elif len(kwargs) > 0:  # Polynomials represented as keyword arguments
            for index, polynomial in kwargs.items():
                index = index[1:]
                self.polynomials[index] = polynomial

    def get_equation(self):
        """
        Creates equation from list of polynomials
        :return: string with equation
        """
        self.polynomials = dict(sorted(self.polynomials.items(), reverse=True))
        string = ""

        for index, polynomial in self.polynomials.items():
            polynomial = int(polynomial)
            index = int(index)

            if polynomial != 0:
                if polynomial < 0:
                    string_pre = " - "
                else:
                    string_pre = " + "

                if index != 0:
                    string_append = "x"
                elif polynomial == 1 or polynomial == -1:
                    string_append = str(abs(polynomial))
                else:
                    string_append = ""

                if polynomial < 0:
                    polynomial = abs(polynomial)

                if polynomial != 1:
                    string_append = str(polynomial) + string_append

                if index != 0 and index != 1:
                    string_append += "^" + str(index)

                string += string_pre + string_append

        if len(string) > 0:
            string = string[3:]
        else:
            string = "0"

        return string

    def __str__(self):
        """
        Magic method for string
        :return: string equation of polynomials
        """
        return self.get_equation()

    def __eq__(self, other):
        """
        Checks if two Polynomials are equal
        :param other: Other Polynomial
        """
        return str(self) == str(other)

    def __add__(self, other):
        """
        Adds polynomial with other polynomial
        :param other: Other Polynomial
        """
        attributes = {}

        for index, polynomial in self.polynomials.items():
            attributes["x" + str(index)] = polynomial

        for index, polynomial in other.polynomials.items():
            if index in self.polynomials:
                attributes["x" + str(index)] = self.polynomials[index] + polynomial
            else:
                attributes["x" + str(index)] = polynomial

        return Polynomial(**attributes)

    def factorial(self, n):
        """
        Calculates n factorial
        :param n: number for factorial
        :return: factorial of n
        """
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def calculate_combinatorial_number(self, n, k):
        """
        Calculated combinatorial number for n above k
        :param n: number
        :param k: number
        :return: combinatorial number for n above k
        """
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def __pow__(self, power):
        """
        Pow magic method for Polynomial
        :param power
        :return: Returns Polynomial powered by power
        """
        if power == 1:
            return self
        elif power == 0:
            return Polynomial(1)

        self.polynomials = {key: val for key, val in self.polynomials.items() if val != 0}
        self.polynomials = dict(sorted(self.polynomials.items(), reverse=True))

        attributes = {}

        # Using Binomial theorem
        n = 0
        m = power
        use_n = True

        for k in range(0, power + 1):
            result = self.calculate_combinatorial_number(power, k)

            for index, polynomial in self.polynomials.items():
                if use_n:
                    result *= pow(polynomial, (power - n))
                    n += 1
                    use_n = False
                else:
                    result *= pow(polynomial, (power + m))
                    m -= 1
                    use_n = True

            attributes["x" + str(n - 1)] = result

        return Polynomial(**attributes)

    def derivative(self):
        """
        Derivates Polynomial
        :return: Derivated Polynomial
        """
        attributes = {}

        for index, polynomial in self.polynomials.items():
            if int(index) > 0:
                attributes["x" + str(int(index) - 1)] = polynomial * int(index)

        return Polynomial(**attributes)

    def calculate(self, x):
        """
        Calculates result of Polynomial equation
        :param x: equation variable
        :return: result of equation
        """
        result = 0

        for index, polynomial in self.polynomials.items():
            result += polynomial * pow(x, int(index))

        return result

    def at_value(self, first, second=None):
        """
        Calculates Polynomial equation.
        If second variable is set, returns result of second value subtracted by result of first value
        :param first: First equation variable
        :param second: Second equation variable
        :return: Result of Polynomial equation at values
        """
        result = self.calculate(first)

        if second is not None:
            result = self.calculate(second) - result

        return result


def test():
    """
    Function for tests using asserts
    """
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


if __name__ == '__main__':
    test()
