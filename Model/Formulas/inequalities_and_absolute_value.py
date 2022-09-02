

class InequalitiesAndAbsoluteValue:
    @staticmethod
    def get_all_rules():
        rule = "if a < b and b < c then a < c\n"
        rule += "if a < b then a + c < b + c\n"
        rule += "if a < b and c > 0 then ac < bc\n"
        rule += "if a < b and c < 0 then bc < ac\n"
        rule += "if a > 0, then\n"
        rule += " " * 10 + " |x| = a means x = a or x = -a\n"
        rule += " " * 10 + " |x| < a means -a < x < a\n"
        rule += " " * 10 + " |x| > a means x > a or x < -a"
        return rule
