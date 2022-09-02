from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from View.MathGroundBox.MiddleBox.RightBox.right_bar_scroll_view import RightBarScrollView

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\RightBox\\kv\\right_bar.kv")


class RightBar(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(RightBarScrollView())