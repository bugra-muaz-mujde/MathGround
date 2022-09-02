from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class PowerRuleWithRadicalsRootOfProducts(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('The product of two numbers to')
        first_equality1 = Text('the power divided by one')
        second_equality = Text("=")
        third_equality = Text("The product of their")
        third_equality1 = Text("power divided by one")
        equation = Tex(
            r'$\sqrt[\leftroot{-2}\uproot{2}n]{(x.y)}=\sqrt[\leftroot{-2}\uproot{2}n]{x}.\sqrt[\leftroot{-2}\uproot{2}n]{y}$').scale(3)

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


#  manim -pql power_rule_with_radicals_root_of_products.py PowerRuleWithRadicalsRootOfProducts
