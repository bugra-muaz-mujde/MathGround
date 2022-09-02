from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class PowerRuleWithRadicalsRootOfRoot(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('The root of the root of a number')
        second_equality = Text("=")
        third_equality = Text('The root of the product of')
        forth_equality = Text('the root powers of that number')
        equation = Tex(
            r'$\sqrt[\leftroot{-2}\uproot{2}n]{\sqrt[\leftroot{-2}\uproot{2}m]{x}}=\sqrt[\leftroot{-2}\uproot{2}m]{\sqrt[\leftroot{-2}\uproot{2}n]{x}}=\sqrt[\leftroot{-2}\uproot{2}m.n]{x}$').scale(2)

        first_equality.next_to(first_equality, UP * 2)
        second_equality.next_to(first_equality, DOWN)
        third_equality.next_to(second_equality, DOWN)
        forth_equality.next_to(third_equality, DOWN)
        self.play(Write(first_equality), Write(second_equality), Write(third_equality), Write(forth_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation), FadeOut(second_equality, third_equality, forth_equality))
        self.wait(3)


#  manim -pql power_rule_with_radicals_root_of_root.py PowerRuleWithRadicalsRootOfRoot
