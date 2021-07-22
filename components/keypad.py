from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from components.base import DroButton
import logging

log = logging.getLogger()


class KeypadPanel(BoxLayout):
    current_value = StringProperty()

    def __init__(self, **kwargs):
        super(KeypadPanel, self).__init__(**kwargs)

        self.register_event_type('on_enter')
        self.size_hint_x = 0.6
        self.orientation = "vertical"
        keypad_layout = GridLayout(cols=4)
        self.keys = dict(
            key_7=DroButton(text="7"),
            key_8=DroButton(text="8"),
            key_9=DroButton(text="9"),
            key_back=DroButton(text="<-"),
            key_4=DroButton(text="4"),
            key_5=DroButton(text="5"),
            key_6=DroButton(text="6"),
            key_clear=DroButton(text="CLR"),
            key_1=DroButton(text="1"),
            key_2=DroButton(text="2"),
            key_3=DroButton(text="3"),
            key_free_1=DroButton(text=""),
            key_free_2=DroButton(text=""),
            key_0=DroButton(text="0"),
            key_comma=DroButton(text="."),
            key_enter=DroButton(text="OK"),
        )
        for key in self.keys.values():
            key.bind(on_press=self.key_pressed)
            keypad_layout.add_widget(key)

        self.add_widget(keypad_layout)

    def key_pressed(self, instance):
        if instance.text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            self.current_value = str(self.current_value) + str(instance.text)
        if instance.text == "CLR":
            self.current_value = ""
        if instance.text == "<-":
            self.current_value = str(self.current_value[:-1])
        if instance.text == "OK":
            self.dispatch("on_enter", True)

    def on_enter(self, value):
        pass