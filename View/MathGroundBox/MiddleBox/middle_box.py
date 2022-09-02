from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy_widget_finder_1queque_t.kivy_widget_finder import KivyWidgetFinder
from Service.chapter_service import ChapterService
from View.MathGroundBox.MiddleBox.CenterBox.center_box import CenterBox
from View.MathGroundBox.MiddleBox.LeftBox.left_bar import LeftBar
from View.MathGroundBox.MiddleBox.RightBox.right_bar import RightBar
from View.MathGroundBox.MiddleBox.sub_chapter_button import SubChapterButton
from View.MathGroundBox.chapter_button import ChapterButton

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\kv\\middle_box.kv")


class MiddleBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LeftBar())
        self.add_widget(CenterBox())
        self.add_widget(RightBar())

    def add_sub_chapters_to_bars(self, main_chapter):
        left_bar_bucket = KivyWidgetFinder(self).find_widgets_and_get_list_from_class("LeftBarScrollViewBucket")[0]
        left_bar_bucket.clear_widgets(left_bar_bucket.children)
        chapters = ChapterService.read_predict_from_csv()
        for index, chapter in enumerate(chapters):
            if chapter[main_chapter]:
                left_bar_bucket.add_widget(SubChapterButton(chapter[main_chapter], main_chapter))
