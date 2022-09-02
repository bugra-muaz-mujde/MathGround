import math
import time


class ExponentsAndRadicals:
    @staticmethod
    def product_rule_with_same_base():
        rule1 = "Product of same base with different powers = Sum of different powers of a number\n"
        example = "(x**m) * (x**n) = x**(m + n)"
        return rule1 + example

    @staticmethod
    def product_rule_with_same_exponent():
        rule1 = "Product of same base with same power = Same power of the product of numbers\n"
        example = "(x * y)**n = (x**n) * (y**n)"
        return rule1 + example

    @staticmethod
    def quotient_rule_with_same_base():
        rule1 = "Division of different powers of same number = Difference of different powers of a number\n"
        example = "(x**m) / (x**n) = x**(m - n)"
        return rule1 + example

    @staticmethod
    def quotient_rule_with_same_exponents():
        rule1 = "The power of the quotients of different numbers = The quotients of the powers of the numbers\n"
        example = "(x / y)**n = (x**n) / (y**n)"
        return rule1 + example

    @staticmethod
    def negative_exponents_rule():
        rule1 = "Negative power of a number = The number divided by one\n"
        example = "x**(-1 * n) = 1 / (x**n)"
        return rule1 + example

    @staticmethod
    def power_rule():
        rule1 = "The power of the power of a number = The product of the powers of that number\n"
        example = "(x**m)**n = x**(m * n)"
        return rule1 + example

    @staticmethod
    def power_rule_with_radicals_root_of_products():
        rule1 = "The product of two numbers to the power divided by one = The product of their power divided by one\n"
        example = "(x * y)**(1 / n) = (x**(1 / n)) * (y**(1 / n))"
        return rule1 + example

    @staticmethod
    def power_rule_with_radicals_root_of_root():
        rule1 = "The root of the root of a number = The root of the product of the root powers of that number\n"
        example = "(x**(1 / m))**(1 / n) = (x**(1 / n))**(1 / m) = x**(1 / (m * n))"
        return rule1 + example

    @staticmethod
    def power_rule_with_radicals_power_of_root():
        rule1 = "The numerator and denominator of the power of a number = The denominator root of the numerator power of that number\n"
        example = "x**(m / n) = (x**m)**(1 / n)"
        return rule1 + example

    @staticmethod
    def power_rule_with_radicals_the_root():
        rule1 = "The power of a number divided by one = The root of that number\n"
        example = "x**(1 / n) = n root x"
        return rule1 + example

    @staticmethod
    def power_rule_with_radicals_quotient_of_roots():
        rule1 = "The roots of the quotients of two numbers = The quotients of the roots of those numbers\n"
        example = "(x / y)**(1 / n) = (x**(1 / n) / y**(1 / n))"
        return rule1 + example

    def get_all_rules(self):
        self.product_rule_with_same_base()
        self.product_rule_with_same_exponent()
        self.quotient_rule_with_same_base()
        self.quotient_rule_with_same_exponents()
        self.negative_exponents_rule()
        self.power_rule()
        self.power_rule_with_radicals_the_root()
        self.power_rule_with_radicals_root_of_root()
        self.power_rule_with_radicals_power_of_root()
        self.power_rule_with_radicals_root_of_products()
        self.power_rule_with_radicals_quotient_of_roots()


def is_perfect_square(number):
    iterate = 0
    difference = 1
    while number > 0:
        number = number - difference
        difference += 2
        iterate += 1
    if number == 0:
        return iterate
    else:
        return None


def list_of_perfect_squares_in_given_range(given_range):
    perfect_squares = []
    number = 0
    for increase_number in range(1, given_range, 2):
        number += increase_number
        perfect_squares.append(number)
        if number > given_range:
            break
    return perfect_squares

