

class SpecialProducts:
    @staticmethod
    def product_rule_the_square_of_sum_of_two_numbers():
        return "(x + y)**2 = (x**2 + 2xy + y**2)"

    @staticmethod
    def product_rule_the_square_of_difference_of_two_numbers():
        return "(x - y)**2 = (x**2 - 2xy + y**2)"

    @staticmethod
    def product_rule_the_cube_of_sum_of_two_numbers():
        return "(x + y)**3 = (x**3 + 3(x**2)y + 3x(y**2) + y**3)"

    @staticmethod
    def product_rule_the_cube_of_difference_of_two_numbers():
        return "(x - y)**3 = (x**3 - 3(x**2)y + 3x(y**2) - y**3)"

    def get_all_rules(self):
        self.product_rule_the_square_of_sum_of_two_numbers()
        self.product_rule_the_square_of_difference_of_two_numbers()
        self.product_rule_the_cube_of_sum_of_two_numbers()
        self.product_rule_the_cube_of_difference_of_two_numbers()
