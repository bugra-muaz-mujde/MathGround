from manim import *
import numpy as np
from manim.mobject import text

config.pixel_height = 1000
config.pixel_width = 1200


class NegativeExponentsRule(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Negative power of a number')
        second_equality = Text("=")
        third_equality = Text("The number divided by one")
        equation = Tex(
            r'$x^{-n}=\dfrac{1}{x^n}$').scale(3)

        first_equality.next_to(first_equality, UP * 2)
        second_equality.next_to(first_equality, DOWN)
        third_equality.next_to(second_equality, DOWN)
        self.play(Write(first_equality), Write(second_equality), Write(third_equality))
        self.wait(1)
        self.play(ReplacementTransform(third_equality, equation), FadeOut(first_equality, second_equality))
        self.wait(3)


#  manim -pql negative_exponents_rule.py NegativeExponentsRule
