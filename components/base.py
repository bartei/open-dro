from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class DroButton(Button):
    def __init__(self, **kwargs):
        super(DroButton, self).__init__(**kwargs)
        self.font_name = "fonts/Manrope-Bold.ttf"
        self.font_size = 16


class DroToggleButton(ToggleButton):
    def __init__(self, axis_group: str, **kwargs):
        super().__init__(**kwargs)
        self.group = axis_group
