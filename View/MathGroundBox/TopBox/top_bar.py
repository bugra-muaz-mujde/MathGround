from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\TopBox\\kv\\top_bar.kv")


class TopBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
