from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class ProductRuleWithSameExponent(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Product of same base with same power')
        second_equality = Text("=")
        third_equality = Text("Same power of the product of numbers")
        equation = Tex(
            r'$(x.y)^n=x^n.y^n$').scale(3)

        first_equality.next_to(first_equality, UP * 2)
        second_equality.next_to(first_equality, DOWN)
        third_equality.next_to(second_equality, DOWN)
        self.play(Write(first_equality), Write(second_equality), Write(third_equality))
        self.wait(1)
        self.play(ReplacementTransform(third_equality, equation), FadeOut(first_equality, second_equality))
        self.wait(3)


#  manim -pql product_rule_with_same_exponent.py ProductRuleWithSameExponent
