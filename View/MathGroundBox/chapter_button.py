from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy_widget_finder_1queque_t.kivy_widget_finder import KivyWidgetFinder

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\kv\\chapter_button.kv")


class ChapterButton(ButtonBehavior, Label):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.color = 0, 0, 0, 1

    def on_press(self):
        middle_box = KivyWidgetFinder(self).find_widgets_and_get_list_from_class("MiddleBox")[0]
        middle_box.add_sub_chapters_to_bars(self.text)
