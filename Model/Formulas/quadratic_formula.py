

class QuadraticFormula:
    @staticmethod
    def get_roots(a, b, c):
        x1 = (-b + ((b**2) - (4 * a * c))**(1 / 2)) / (2 * a)
        x2 = (-b - ((b**2) - (4 * a * c))**(1 / 2)) / (2 * a)
        return x1, x2

    @staticmethod
    def quadratic_formula_rule():
        rule = "(-b + ((b**2) - (4 * a * c))**(1 / 2)) / (2 * a) and (-b - ((b**2) - (4 * a * c))**(1 / 2)) / (2 * a)"
        return rule
