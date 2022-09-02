from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer

Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\MathGroundBox\\MiddleBox\\CenterBox\\kv\\center_box_video_player.kv")


class CenterBoxVideoPlayer(VideoPlayer):
    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)
        self.source = source
        self.state = "play"
        self.options = {'eos': 'loop'}
        self.allow_stretch = False
