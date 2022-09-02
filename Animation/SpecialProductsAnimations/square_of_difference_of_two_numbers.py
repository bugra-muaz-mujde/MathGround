from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class SquareOfDifferenceOfTwoNumbersAnimation(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Square of difference of two numbers')
        equation = Tex(
            r'$(x - y)^2=(x^2 - 2xy + y^2)$').scale(1.5)

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql square_of_difference_of_two_numbers.py SquareOfDifferenceOfTwoNumbersAnimation
