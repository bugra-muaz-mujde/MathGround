from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class QuotientRuleWithSameBase(Scene):
    def construct(self):
        first_equality = Text('Division of different')
        first_equality1 = Text('powers of same number')
        second_equality = Text("=")
        third_equality = Text("Difference of different")
        third_equality1 = Text("powers of a number")
        equation = Tex(
            r'$\dfrac{(x^m)}{(x^n)}=x^{(m - n)}$').scale(3)

        first_equality.next_to(first_equality, UP * 4)
        first_equality1.next_to(first_equality, DOWN)
        second_equality.next_to(first_equality1, DOWN)
        third_equality.next_to(second_equality, DOWN)
        third_equality1.next_to(third_equality, DOWN)
        self.play(
            Write(first_equality),
            Write(first_equality1),
            Write(second_equality),
            Write(third_equality),
            Write(third_equality1)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(third_equality, equation),
            FadeOut(
                first_equality,
                first_equality1,
                second_equality,
                third_equality1,
            )
        )
        self.wait(3)

#  manim -pql quotient_rule_with_same_base.py QuotientRuleWithSameBase
