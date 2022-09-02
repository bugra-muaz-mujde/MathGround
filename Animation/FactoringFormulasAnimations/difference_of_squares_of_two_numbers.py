from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class DifferenceOfSquaresOfTwoNumbersAnimation(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Difference of squares of two numbers')
        equation = Tex(
            r'$(x^2 - y^2)=(x + y)(x - y)$').scale(1.5)

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql difference_of_squares_of_two_numbers.py DifferenceOfSquaresOfTwoNumbersAnimation
