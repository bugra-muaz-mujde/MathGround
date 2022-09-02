from manim import *
import numpy as np

config.pixel_height = 1000
config.pixel_width = 1200


class CoordsToPointExample(Scene):
    def __init__(self):
        super().__init__()

    def construct(self):
        ax = Axes(x_range=[-10, 11, 1], y_range=[-10, 11, 1], y_length=10).add_coordinates()
        self.add(ax)


class DisplayEquations(Scene):
    def construct(self):
        # Create Tex objects
        first_line = Text('Manim also allows you')
        second_line = Text('to show beautiful math equations')
        equation = Tex(
            r'$d\left(p, q\right)=d\left(q, p\right)=\sqrt{(q_1-p_1)^2+(q_2-p_2)^2+...+(q_n-p_n)^2}=\sqrt{\sum_{i=1}^n\left(q_i-p_i\right)^2}$')

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)
