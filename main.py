from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutSample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     button1 = Button(text= "button1")
    #     button2 = Button(text= "button2")
    #     self.add_widget(button1)
    #     self.add_widget(button2)
    #     self.orientation = "vertical"

class MainWidget(Widget):
    pass

class TcgGuiApp(App):
    pass

TcgGuiApp().run()