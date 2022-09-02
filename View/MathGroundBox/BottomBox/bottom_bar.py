from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\BottomBox\\kv\\bottom_bar.kv")


class BottomBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
