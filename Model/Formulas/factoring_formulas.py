

class FactoringFormulas:
    @staticmethod
    def factoring_rule_difference_of_squares_of_two_numbers():
        return "(x**2 - y**2) = (x + y)(x - y)"

    @staticmethod
    def factoring_rule_sum_of_cubes_of_two_numbers():
        return "(x**3 + y**3) = (x + y)(x**2 - xy + y**2)"

    @staticmethod
    def factoring_rule_difference_of_cubes_of_two_numbers():
        return "(x**3 - y**3) = (x - y)(x**2 + xy + y**2)"

    def get_all_rules(self):
        self.factoring_rule_difference_of_squares_of_two_numbers()
        self.factoring_rule_sum_of_cubes_of_two_numbers()
        self.factoring_rule_difference_of_cubes_of_two_numbers()