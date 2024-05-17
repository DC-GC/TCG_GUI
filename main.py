from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class AnchorLayoutExample(AnchorLayout):
    pass
class CardEntry(BoxLayout):
    pass

class BoxLayoutSample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     button1 = Button(text= "button1")
    #     button2 = Button(text= "button2")
    #     self.add_widget(button1)
    #     self.add_widget(button2)
    #     self.orientation = "vertical"

class MainWidget(BoxLayout):
    pass

class TcgGuiApp(App):
    pass

TcgGuiApp().run()