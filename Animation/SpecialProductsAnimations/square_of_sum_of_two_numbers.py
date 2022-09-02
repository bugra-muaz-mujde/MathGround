from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class SquareOfSumOfTwoNumbersAnimation(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Squares of sum of two numbers')
        equation = Tex(
            r'$(x + y)^2=(x^2 + 2xy + y^2)$').scale(1.5)

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql square_of_sum_of_two_numbers.py SquareOfSumOfTwoNumbersAnimation
