from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):
    def build(self):
        self.operators = ["/", "*", "-", "+"]
        self.last_operator = None
        self.last_dot = False
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="green", foreground_color="grey",
                                  halign="right", multiline=False, font_size=55, readonly=True)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"]
        ]
        for set in buttons:
            v_layout = BoxLayout()
            for text in set:
                button = Button(
                    text=text, font_size=33, background_color="yellow",
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_press)
                v_layout.add_widget(button)
            main_layout.add_widget(v_layout)
        equal = Button(
                text="=", font_size=33, background_color="yellow",
                pos_hint={"center_x": 0.5, "center_y": 0.5})
        equal.bind(on_press=self.evaluate)
        main_layout.add_widget(equal)

        return main_layout

    def on_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "C":
            self.solution.text = ""
            self.last_dot = False
        elif self.last_dot is True and button_text == ".":
            return
        else:
            if current and (self.last_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.solution.text = current + button_text
            if self.last_dot is False:
                self.last_dot = button_text == "."
            elif self.last_operator is True:
                self.last_dot = False
            self.last_operator = button_text in self.operators

    def evaluate(self, instance):
        text = self.solution.text
        if self.last_operator:
            return
        if text:
            solution = str(eval(text))
            self.solution.text = solution


if __name__ == "__main__":
    app = Calculator()
    app.run()
