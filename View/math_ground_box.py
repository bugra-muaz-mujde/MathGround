import time

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy_widget_finder_1queque_t.kivy_widget_finder import KivyWidgetFinder
from Service.chapter_service import ChapterService
from View.MathGroundBox.BottomBox.bottom_bar import BottomBar
from View.MathGroundBox.MiddleBox.middle_box import MiddleBox
from View.MathGroundBox.TopBox.top_bar import TopBar
from View.MathGroundBox.chapter_button import ChapterButton

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\kv\\math_ground_box.kv")


class MathGroundBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TopBar())
        self.add_widget(MiddleBox())
        self.add_widget(BottomBar())
        self.add_chapters_to_bars()
        self.kivy_widget_finder = None

    def add_chapters_to_bars(self):
        chapters = ChapterService.read_predict_from_csv()
        for index, chapter in enumerate(chapters.fieldnames):
            if index < len(chapters.fieldnames) // 2:
                self.children[2].add_widget(ChapterButton(chapter))
            else:
                self.children[0].add_widget(ChapterButton(chapter))
