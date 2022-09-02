from manim import *
config.pixel_height = 1000
config.pixel_width = 1200


class CubeOfDifferenceOfTwoNumbersAnimation(Scene):
    def construct(self):
        # Create Tex objects
        first_equality = Text('Cube of difference of two numbers')
        equation = Tex(
            r'$(x - y)^3=(x^3 - 3x^2y + 3xy^2 - y^3)$').scale(1.5)

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, equation))
        self.wait(3)


#  manim -pql cube_of_difference_of_two_numbers.py CubeOfDifferenceOfTwoNumbersAnimation
