from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label
from Service.sub_chapter_service import SubChapterService
from kivy_widget_finder_1queque_t.kivy_widget_finder import KivyWidgetFinder

from View.MathGroundBox.MiddleBox.RightBox.sub_chapter_of_sub_chapter_button import SubChapterOfSubChapterButton

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\kv\\sub_chapter_button.kv")


class SubChapterButton(ButtonBehavior, Label):
    def __init__(self, text, main_text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.color = 0, 0, 0, 1
        self.main_text = main_text

    def on_press(self):
        sub_chapter_of_sub_chapter_list = SubChapterService(self.main_text, self.text).get_sub_chapters()
        self.add_sub_chapter_to_right_bar(sub_chapter_of_sub_chapter_list)

    def add_sub_chapter_to_right_bar(self, sub_chapter):
        right_bar_bucket = KivyWidgetFinder(self).find_widgets_and_get_list_from_class("RightBarScrollViewBucket")[0]
        right_bar_bucket.clear_widgets(right_bar_bucket.children)
        print(sub_chapter)
        for chapter in sub_chapter:
            right_bar_bucket.add_widget(SubChapterOfSubChapterButton(chapter.split(".mp4")[0], self.main_text, self.text))

