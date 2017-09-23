# -*- coding: utf-8 -*-
"""
@author: phancuong
"""
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Line, Color
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
# Global Variable to get color is choosed
Colour = [0,0,0,1]

# Funtion that will update color for Dropdown buttoon
def Color_Text(color):
    
    if (color == 'Red'):
        color_text = [1,0,0,1]
    elif (color == 'Blue'):
        color_text = [0,0,1,1]
    elif (color == 'Green'):
        color_text = [0,1,0,1]
    elif (color == 'Yellow'):
        color_text = [1,1,0,1]
    else:
        color_text = [1,1,1,1]
    return color_text

class MainScreen(Screen):
    
    def __init__(self, **kwargs):   
        super(MainScreen, self).__init__(**kwargs)
        # GridLayout prepare for next developing
        self.grid_layout = GridLayout(cols=2, row_force_default=True, row_default_height=20)
        # create a dropdown and set reaction when choose one of DropDown
        # While choose , the color of mainbutton will change corressponding DropDown
        self.dropdown = DropDown()
        types = ['Red', 'Blue', 'Green', 'Yellow', 'White']   
        for i in types:            
            btn = Button(text=i, size_hint_y=None, height=20,
                         font_size='14sp',color=Color_Text(i))
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.color))
            # Add some object to DropDown
            self.dropdown.add_widget(btn)
        self.dropdown.bind(on_select=lambda instance, x: self.ChooseDropDown( x=x))
        # Create a mainbutton that opens DropDown when pressing
        self.mainbutton = Button(text='Color',size_hint_x=None, width=100,
                                 height=20, color=[1,0.5,0.5,1])
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.grid_layout.add_widget(self.mainbutton)
        self.add_widget(self.grid_layout)
    
    # The fucntion will change text color of mainbutton
    # and set global variable Colour
    def ChooseDropDown(self, x):
        global Colour
        setattr(self.mainbutton, 'color', x)
        Colour = x
        
class AnotherScreen(Screen):
    pass

class CustomDropDown(DropDown):
    pass

class ScreenManagement(ScreenManager):
    pass

class Widgets(Widget): 
    
    def __init__(self, **kwargs):
        super(Widgets,self).__init__(**kwargs)        
        pass
    
    # When touch the widget, color will get the current text color of mainbutton
    # then use it for canvas
    def on_touch_down(self, touch):
        global Colour
        color = Colour
        self.R = color[0]
        self.G = color[1]
        self.B = color[2]
        self.A = 1
        with self.canvas:
            Color(self.R, self.G, self.B, self.A)
            touch.ud["line"] = Line(points=(touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)
        
presentation = Builder.load_file("awesome.kv")

class AwesomeApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":

    AwesomeApp().run()
    
