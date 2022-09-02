from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from View.MathGroundBox.MiddleBox.LeftBox.left_bar_scroll_view import LeftBarScrollView

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\LeftBox\\kv\\left_bar.kv")


class LeftBar(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LeftBarScrollView())

