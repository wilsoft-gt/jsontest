import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require("1.11.0")
sm = ScreenManager()

class menu(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.screens1 = Button(text="Screen 1")
        self.screens1.bind(on_press=self.goto_screen1)
        self.add_widget(self.screens1)
        self.screens2 = Button(text="Screen 2")
        self.screens2.bind(on_press=self.goto_screen2)
        self.add_widget(self.screens2)


    def goto_screen1(self, *args):
        menu_instance.screen_manager.transition.direction = 'left'
        menu_instance.screen_manager.current = "gtscr1"

    def goto_screen2(self, *args):
        menu_instance.screen_manager.transition.direction = 'left'
        menu_instance.screen_manager.current = "gtscr2"

class Screen1(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Screen 1"))
        self.add_widget(Label(text=""))
        self.add_widget(Label(text="Label 1"))
        self.add_widget(Label(text="Label 1 text"))
        self.add_widget(Label(text="Label 2"))
        self.add_widget(Label(text="Label 2 text"))
        self.add_widget(Label(text="Label 3"))
        self.add_widget(Label(text="Label 3 text"))

        self.mainmenu = Button(text="Menu")
        self.mainmenu.bind(on_press=self.gotomenu)
        self.add_widget(self.mainmenu)

    def gotomenu(self, *args):
        menu_instance.screen_manager.current = "menu"

class Screen2(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="Screen 2"))
        self.add_widget(Label(text=""))
        self.add_widget(Label(text="Label 1"))
        self.add_widget(Label(text="Label 1 text"))
        self.add_widget(Label(text="Label 2"))
        self.add_widget(Label(text="Label 2 text"))
        self.add_widget(Label(text="Label 3"))
        self.add_widget(Label(text="Label 3 text"))

        self.mainmenu = Button(text="Menu")
        self.mainmenu.bind(on_press=self.gotomenu)
        self.add_widget(self.mainmenu)
    
    def gotomenu(self, *args):
        menu_instance.screen_manager.transition.direction = 'right'
        menu_instance.screen_manager.current = "menu"


class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.gtmenu = menu()
        screen = Screen(name="menu")
        screen.add_widget(self.gtmenu)
        self.screen_manager.add_widget(screen)

        self.screen1 = Screen1()
        screen = Screen(name="gtscr1")
        screen.add_widget(self.screen1)
        self.screen_manager.add_widget(screen)

        self.screen2 = Screen2()
        screen = Screen(name="gtscr2")
        screen.add_widget(self.screen2)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    menu_instance = MainApp()
    menu_instance.run()