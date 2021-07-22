import os

import redis
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, DictProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# Initialize a redis client to read the axis coordinates
from components.base import DroButton
from components.coordwidget import CoordWidget
from components.keypad import KeypadPanel
from lib import settings
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class ReferencePanel(BoxLayout):
    origin_id = NumericProperty({})
    tool_id = DictProperty({})


class CoordinatesPanel(BoxLayout):
    selected_axis = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(CoordinatesPanel, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.axis_list = list()
        for axis_name in ["X", "Y", "Z", "A"]:
            axis = CoordWidget(axis_name, "main_group")
            axis.axis_pos = 0.0
            axis.selector.bind(on_press=self.on_axis_selection)
            self.axis_list.append(axis)
            self.add_widget(axis)

    def on_axis_selection(self, instance):
        print("axis selected")
        if instance.state == 'down':
            self.selected_axis = instance.parent
        else:
            self.selected_axis = None


class CommandsPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(CommandsPanel, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 80
        self.bt_settings = DroButton()
        self.bt_settings.text = "Settings"
        self.add_widget(self.bt_settings)
        self.add_widget(DroButton())
        self.add_widget(DroButton())
        self.add_widget(DroButton())
        self.add_widget(DroButton())
        self.add_widget(DroButton())
        self.add_widget(TextInput())


class DashboardTop(BoxLayout):
    current_value = StringProperty()

    def __init__(self, **kwargs):
        super(DashboardTop, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.coordinates = CoordinatesPanel()
        self.coordinates.bind(selected_axis=self.on_selected_axis)

        self.keypad = KeypadPanel()
        self.keypad.bind(current_value=self.on_keypad_value)
        self.keypad.bind(on_enter=self.on_keypad_enter)
        self.add_widget(self.coordinates)
        self.add_widget(self.keypad)

    def on_keypad_value(self, instance, value):
        if self.coordinates.selected_axis is not None:
            self.coordinates.selected_axis.axis_offset = float("0"+self.keypad.current_value)
        print(value)

    def on_keypad_enter(self, instance, value):
        self.coordinates.selected_axis.axis_offset = (
            float("0"+self.keypad.current_value) -
            self.coordinates.selected_axis.axis_pos
        )
        self.coordinates.selected_axis.selector.state = "normal"
        self.coordinates.selected_axis.displayed_value = "POS"
        self.coordinates.selected_axis = None
        print("OK Pressed on keypad")

    def on_selected_axis(self, instance, axis):
        if axis is not None:
            self.keypad.current_value = ""
            self.coordinates.selected_axis.axis_offset = 0.0
            self.coordinates.selected_axis.displayed_value = "OFFSET"


class DroDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super(DroDashboard, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.dashboard_top = DashboardTop()
        self.add_widget(self.dashboard_top)

        self.commands = CommandsPanel()
        self.add_widget(self.commands)

    def update(self, dt):
        for axis in self.dashboard_top.coordinates.axis_list:
            if axis is not self.dashboard_top.coordinates.selected_axis:
                axis: CoordWidget
                axis_pos = redis_client.get(axis.selector.text) or 0
                axis.axis_pos = float(axis_pos) / 200


class DroApp(App):
    def build(self):
        dro = DroDashboard()
        Clock.schedule_interval(dro.update, 1.0 / float(os.environ['KCFG_GRAPHICS_MAXFPS']))
        return dro


if __name__ == "__main__":
    DroApp().run()
