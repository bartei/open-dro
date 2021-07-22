from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from components.base import DroButton, DroToggleButton


class CoordWidget(BoxLayout):
    format = StringProperty("{:+.3f}")
    axis_pos = NumericProperty(0.0)
    axis_offset = NumericProperty(0.0)
    tool_offset = NumericProperty(0.0)

    displayed_value = StringProperty(defaultvalue="POS")

    def __init__(self, axis_label: str, axis_group: str, **kwargs):
        super(CoordWidget, self).__init__(**kwargs)
        self.orientation = "horizontal"

        self.selector = DroToggleButton(axis_group)
        self.selector.text = axis_label
        self.selector.font_size = 72
        self.selector.size_hint_x = 0.2
        self.selector.size_hint_min_x = 80
        self.selector.font_name = "fonts/DSEG14Classic-Italic.ttf"
        # self.selector.bind(on_press=self.on_axis_selected)

        self.value_text = Label()
        self.value_text.font_size = 60
        self.value_text.multiline = False
        self.value_text.font_name = "fonts/DSEG14Classic-Italic.ttf"
        self.value_text.color = (0.2, 1, 0.2, 1)
        self.value_text.width = 0.6

        self.btn_zero = DroButton(
            size_hint_x=0.2,
            size_hint_min_x=80,
            text="Zero"
        )
        self.btn_zero.bind(on_press=self.zero)

        self.add_widget(self.selector)
        self.add_widget(self.value_text)
        self.add_widget(self.btn_zero)

    def on_axis_pos(self, instance, pos):
        self.refresh_text()

    def on_axis_offset(self, instance, pos):
        self.refresh_text()

    def on_tool_offset(self, instance, pos):
        self.refresh_text()

    def on_displayed_value(self, instance, pos):
        self.refresh_text()

    def on_format(self, instance, pos):
        self.refresh_text()

    def zero(self, instance):
        self.axis_offset = 0 - self.axis_pos
        # self.btn_zero.state = "normal"
        if self.selector.state == "down":
            self.selector.state = "normal"
            self.selector.dispatch("on_press")

    def refresh_text(self):
        if self.displayed_value == "POS":
            self.value_text.text = self.format.format(
                self.axis_pos + self.axis_offset + self.tool_offset
            )
        elif self.displayed_value == "OFFSET":
            self.value_text.text = self.format.format(self.axis_offset)
        else:
            self.value_text.text = "ERR"
