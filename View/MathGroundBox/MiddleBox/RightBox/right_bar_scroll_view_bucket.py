from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\RightBox\\kv\\right_bar_scroll_view_bucket.kv")


class RightBarScrollViewBucket(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
