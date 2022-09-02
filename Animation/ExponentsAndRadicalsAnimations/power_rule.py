from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class PowerRule(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('The power of the power of a number')
        second_equality = Text("=")
        third_equality = Text("The product of the powers of that number")
        equation = Tex(
            r'${(x^m)}^n=x^{(m.n)}$').scale(3)

        first_equality.next_to(first_equality, UP * 2)
        second_equality.next_to(first_equality, DOWN)
        third_equality.next_to(second_equality, DOWN)
        self.play(Write(first_equality), Write(second_equality), Write(third_equality))
        self.wait(1)
        self.play(ReplacementTransform(third_equality, equation), FadeOut(first_equality, second_equality))
        self.wait(3)

#  manim -pql power_rule.py PowerRule
