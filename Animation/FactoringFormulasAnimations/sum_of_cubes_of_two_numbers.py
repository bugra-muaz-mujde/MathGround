from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class SumOfCubesOfTwoNumbersAnimation(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Sum of cubes of two numbers')
        equation = Tex(
            r'$(x^3 + y^3)=(x + y)(x^2 - xy + y^2)$').scale(1.5)
        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql sum_of_cubes_of_two_numbers.py SumOfCubesOfTwoNumbersAnimation
