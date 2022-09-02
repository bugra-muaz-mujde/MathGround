from kivy.clock import Clock
from kivy.loader import Loader
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

from Service.sub_chapter_service import SubChapterService

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\CenterBox\\kv\\center_box.kv")


class CenterBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



