from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from View.MathGroundBox.MiddleBox.LeftBox.left_bar_scroll_view_bucket import LeftBarScrollViewBucket
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\LeftBox\\kv\\left_bar_scroll_view.kv")


class LeftBarScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bucket = LeftBarScrollViewBucket()
        self.bucket.bind(minimum_height=self.bucket.setter('height'))
        self.add_widget(self.bucket)
