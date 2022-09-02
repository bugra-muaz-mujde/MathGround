from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class DifferenceOfCubesOfTwoNumbersAnimation(Scene):
    def construct(self):
        first_equality = Text('The roots of the quotients of two numbers = The quotients of the roots of those numbers')
        equation = Tex(
            r'$\sqrt[\leftroot{-2}\uproot{2}n]{\dfrac{x}{y}}=\dfrac{\sqrt[\leftroot{-2}\uproot{2}n]{x}}{\sqrt[\leftroot{-2}\uproot{2}n]{y}}$')
        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql power_rule_with_radicals_quotient_of_roots.py DifferenceOfCubesOfTwoNumbersAnimation
