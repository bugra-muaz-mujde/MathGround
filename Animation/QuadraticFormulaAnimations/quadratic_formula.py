from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class QuadraticFormula(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Quadratic formula of roots').scale(1.5)
        equation = Tex(
            r'$x= \dfrac{-b \mp \sqrt{b^2 - 4ac}}{2a}$').scale(2)

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql quadratic_formula.py QuadraticFormula
