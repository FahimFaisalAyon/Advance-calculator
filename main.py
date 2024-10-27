from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import math

# KV layout as a string
kv_layout = '''
<MainWidget>:
    rows: 10
    display_text: ""

    Label:
        text: root.display_text
        size_hint_y: None
        height: 200

    GridLayout:
        cols: 6
        Button:
            text: "sin"
            on_press: root.click(self.text)
        Button:
            text: "cos"
            on_press: root.click(self.text)
        Button:
            text: "tan"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "√"
            on_press: root.click(self.text)
        Button:
            text: "^"
            on_press: root.click(self.text)

    GridLayout:
        cols: 6
        Button:
            text: "cosec"
            on_press: root.click(self.text)
        Button:
            text: "sec"
            on_press: root.click(self.text)
        Button:
            text: "cot"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "("
            on_press: root.click(self.text)
        Button:
            text: ")"
            on_press: root.click(self.text)

    GridLayout:
        cols: 6
        Button:
            text: "π"
            on_press: root.click(self.text)
        Button:
            text: "e"
            on_press: root.click(self.text)
        Button:
            text: "!"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "log"
            on_press: root.click(self.text)
        Button:
            text: "ln"
            on_press: root.click(self.text)

    Label:
        size_hint_y: None
        height: 10

    GridLayout:
        cols: 6
        Button:
            text: "7"
            on_press: root.click(self.text)
        Button:
            text: "8"
            on_press: root.click(self.text)
        Button:
            text: "9"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "DEL"
            on_press: root.click(self.text)
        Button:
            text: "AC"
            on_press: root.click(self.text)

    GridLayout:
        cols: 6
        Button:
            text: "4"
            on_press: root.click(self.text)
        Button:
            text: "5"
            on_press: root.click(self.text)
        Button:
            text: "6"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "x"
            on_press: root.click(self.text)
        Button:
            text: "/"
            on_press: root.click(self.text)

    GridLayout:
        cols: 6
        Button:
            text: "1"
            on_press: root.click(self.text)
        Button:
            text: "2"
            on_press: root.click(self.text)
        Button:
            text: "3"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "+"
            on_press: root.click(self.text)
        Button:
            text: "-"
            on_press: root.click(self.text)

    GridLayout:
        cols: 6
        Button:
            text: "0"
            on_press: root.click(self.text)
        Button:
            text: "."
            on_press: root.click(self.text)
        Button:
            text: "%"
            on_press: root.click(self.text)
        Label:
            size_hint_x: None
            width: 5
        Button:
            text: "Ans"
            on_press: root.click(self.text)
        Button:
            text: "="
            on_press: root.click(self.text)
'''


class TheLabApp(App):
    def build(self):
        Builder.load_string(kv_layout)  # Load the KV layout
        return MainWidget()


class MainWidget(GridLayout):
    display_text = StringProperty("")  # Bind display_text property

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_answer = ""

    def click(self, button_text):
        if button_text == "AC":
            self.display_text = ""
        elif button_text == "DEL":
            self.display_text = self.display_text[:-1]
        elif button_text == "=":
            if self.display_text.startswith("√"):
                value = float(self.display_text[1:])
                if value < 0:
                    self.display_text = "Error"
                else:
                    y = math.sqrt(value)
                    self.display_text = str(y)
                    self.last_answer = str(y)
            else:
                try:
                    l = str(eval(self.display_text))
                    self.display_text = l
                    self.last_answer = l
                except Exception:
                    self.display_text = "Error"
        elif button_text == "x":
            self.display_text += "*"
        elif button_text == "Ans":
            self.display_text += self.last_answer
        elif button_text == "^":
            self.display_text += "**"
        elif button_text == "π":
            self.display_text += str(math.pi)
        elif button_text == "e":
            self.display_text += str(math.e)
        elif button_text == "√":
            if not self.display_text:
                self.display_text += "√"
        elif button_text == "!":
            try:
                value = int(self.display_text)
                if value >= 0:
                    result = math.factorial(value)
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        elif button_text == "sin":
            try:
                value = float(self.display_text)
                result = math.sin(math.radians(value))
                self.display_text = str(result)
            except ValueError:
                self.display_text = "Error"
        elif button_text == "cos":
            try:
                value = float(self.display_text)
                result = math.cos(math.radians(value))
                self.display_text = str(result)
            except ValueError:
                self.display_text = "Error"
        elif button_text == "tan":
            try:
                value = float(self.display_text)
                result = math.tan(math.radians(value))
                self.display_text = str(result)
            except ValueError:
                self.display_text = "Error"
        elif button_text == "sec":
            try:
                value = float(self.display_text)
                cos_value = math.cos(math.radians(value))
                if cos_value != 0:
                    result = 1 / cos_value
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        elif button_text == "cosec":
            try:
                value = float(self.display_text)
                sin_value = math.sin(math.radians(value))
                if sin_value != 0:
                    result = 1 / sin_value
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        elif button_text == "cot":
            try:
                value = float(self.display_text)
                tan_value = math.tan(math.radians(value))
                if tan_value != 0:
                    result = 1 / tan_value
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        elif button_text == "ln":
            try:
                value = float(self.display_text)
                if value > 0:
                    result = math.log(value)
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        elif button_text == "log":
            try:
                value = float(self.display_text)
                if value > 0:
                    result = math.log10(value)
                    self.display_text = str(result)
                else:
                    self.display_text = "Error"
            except ValueError:
                self.display_text = "Error"
        else:
            self.display_text += button_text


TheLabApp().run()
