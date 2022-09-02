import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.lang import Builder
from View.math_ground_box import MathGroundBox
from kivy.config import Config
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\MathGround\\View\\kv\\math_ground.kv")
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')


class MathGround(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MathGroundBox())


class MathGroundApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return MathGround()


if __name__ == "__main__":
    MathGroundApp().run()
