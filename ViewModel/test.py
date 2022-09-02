from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.extras.highlight import KivyLexer
from kivy.lang.parser import ParserException
from kivy.properties import ColorProperty
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen

import time
import threading
import random

kv = ("""   
FloatLayout:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'test_back.png'

    Image:
        id: intro
        source: 'C:\\deneme1.gif'
        size_hint: None, None
        size: "500dp", "500dp"
        pos_hint: {'center_x':.5, 'center_y':.5}
        allow_stretch: False
        anim_delay: 0.05
        anim_loop: 1

""")

class testApp(App):
    def build(self):
        kivy_design = Builder.load_string(kv)
        self.app_root = kivy_design
        return kivy_design

    def on_start(self):
        frame_counter = 0
        frame_counter += 1
        if frame_counter == 30:
            self.app_root.ids.intro.pos_hint = {'center_x':-.5, 'center_y':-.5}

testApp().run()