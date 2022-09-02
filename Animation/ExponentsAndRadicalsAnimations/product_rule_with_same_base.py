from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class ProductRuleWithSameBase(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Product of same base with different powers = Sum of different powers of a number')
        equation = Tex(
            r'$(x^m)(x^n)=x^{(m+n)}$')

        first_equality = Text('Product of same base')
        first_equality1 = Text('with different powers')
        second_equality = Text("=")
        third_equality = Text("Sum of different powers of a number")
        equation = Tex(
            r'$(x^m)(x^n)=x^{(m+n)}$').scale(3)

        first_equality.next_to(first_equality, UP * 2)
        first_equality1.next_to(first_equality, DOWN)
        second_equality.next_to(first_equality1, DOWN)
        third_equality.next_to(second_equality, DOWN)
        self.play(Write(first_equality), Write(first_equality1), Write(second_equality), Write(third_equality))
        self.wait(1)
        self.play(ReplacementTransform(third_equality, equation), FadeOut(first_equality, first_equality1, second_equality))
        self.wait(3)


#  manim -pql product_rule_with_same_base.py DifferenceOfCubesOfTwoNumbersAnimation
