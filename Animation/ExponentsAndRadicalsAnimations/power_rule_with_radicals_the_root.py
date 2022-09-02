from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class PowerRuleWithRadicalsTheRoot(Scene):
    def construct(self):
        # Create Tex objects

        first_equality = Text('The power of a number divided by one')
        second_equality = Text("=")
        third_equality = Text("The root of that number")
        equation = Tex(
            r'$x^{\dfrac{1}{n}}=\sqrt[\leftroot{-2}\uproot{2}n]{x}$').scale(2)

        first_equality.next_to(first_equality, UP * 2)
        second_equality.next_to(first_equality, DOWN)
        third_equality.next_to(second_equality, DOWN)
        self.play(Write(first_equality), Write(second_equality), Write(third_equality))
        self.wait(1)
        self.play(ReplacementTransform(third_equality, equation), FadeOut(first_equality, second_equality))
        self.wait(3)



#  manim -pql power_rule_with_radicals_the_root.py PowerRuleWithRadicalsTheRoot
