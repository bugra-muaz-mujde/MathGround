from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from View.MathGroundBox.MiddleBox.LeftBox.left_bar_scroll_view_bucket import LeftBarScrollViewBucket
from View.MathGroundBox.MiddleBox.RightBox.right_bar_scroll_view_bucket import RightBarScrollViewBucket

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\RightBox\\kv\\right_bar_scroll_view.kv")


class RightBarScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bucket = RightBarScrollViewBucket()
        self.bucket.bind(minimum_height=self.bucket.setter('height'))
        self.add_widget(self.bucket)
