from manim import *
import numpy as np
config.pixel_height = 1000
config.pixel_width = 1200


class InequalitiesAndAbsoluteValue(Scene):
    def construct(self):
        # Create Tex objects
        count = 4
        first_equality = Text('Inequalities and absolute value')
        rules = [Tex(r'$if\ \ a < b \ \ and \ \ b < c \ \ then: \ \ a < c$').scale(1.5),
                 Tex(r'$if\ \ a < b \ \ then: \ \ a + c < b + c$').scale(1.5),
                 Tex(r'$if\ \ a < b \ \ and \ \ c > 0 \ \ then: \ \ ac < bc$').scale(1.5),
                 Tex(r'$if\ \ a < b \ \ and \ \ c < 0 \ \ then: \ \ bc < ac$').scale(1.5),
                 Tex(r'$if\ \ a > 0, \ \ then:$').scale(1.5),
                 Tex(r'$\lvert x \rvert = a\ \ means \ \ x = a \ \ or \ \ x = -a$').scale(1.3),
                 Tex(r'$\lvert x \rvert < a\ \ means \ \ -a < x < a$').scale(1.3),
                 Tex(r'$\lvert x \rvert > a\ \ means \ \ x > a \ \ or \ \ x < -a$').scale(1.3)
                 ]

        self.play(Write(first_equality))
        self.wait(1)
        self.play(ReplacementTransform(first_equality, rules[0]))
        self.wait(2)
        then_count = 0
        for i in range(len(rules)):
            if i < 5:
                line = Line(DOWN, UP * (count - i))
            else:
                line = Line(UP, DOWN * (i - count))
            if i == 4:
                self.play(ApplyMethod(rules[i].shift, np.array([-2, 0, 0])))
                self.wait(2)
            elif i > 4:
                self.play(ApplyMethod(rules[i].shift, np.array([2, -1 - then_count, 0])))
                then_count += 1
                self.wait(2)
            else:
                self.play(MoveAlongPath(rules[i], line), rate_func=linear)
                self.wait(2)



#  manim -pql inequalities_and_absolute_value.py InequalitiesAndAbsoluteValue
