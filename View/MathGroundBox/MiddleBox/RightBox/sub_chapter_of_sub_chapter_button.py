from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_widget_finder_1queque_t.kivy_widget_finder import KivyWidgetFinder
from Service.sub_chapter_service import SubChapterService
from View.MathGroundBox.MiddleBox.CenterBox.center_box_video_player import CenterBoxVideoPlayer

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\RightBox\\kv\\sub_chapter_of_sub_chapter_button.kv")


class SubChapterOfSubChapterButton(ButtonBehavior, Label):
    def __init__(self, text, main_text, sub_main_text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.color = 0, 0, 0, 1
        self.main_text = main_text
        self.sub_main_text = sub_main_text

    def on_press(self):
        source = SubChapterService(self.main_text, self.sub_main_text).get_sub_chapter_of_sub_chapter_path(self.text)
        self.add_video_player_to_center_box(source)

    def add_video_player_to_center_box(self, source):
        center_box = KivyWidgetFinder(self).find_widgets_and_get_list_from_class("CenterBox")[0]
        center_box.clear_widgets(center_box.children)
        center_box.add_widget(CenterBoxVideoPlayer(source))

