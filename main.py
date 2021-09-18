from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty


class Whole(BoxLayout):

    my_text = StringProperty("")
    first = StringProperty("")
    second= StringProperty("")
    '''
    def dod(self):
        self.second = self.my_text
        self.my_text = str(float(self.my_text)+float(self.second))
        self.second=self.my_text
        self.second = "0"
    def minus(self):
        self.my_text = str(float(self.my_text)-float(self.second))
        self.second = self.my_text
        self.second = "0"
    def multiple(self):
        self.my_text = str(float(self.my_text)*float(self.second))
        self.second = self.my_text
        self.second = "0"
    def podziel(self):
        self.my_text = str(float(self.my_text)/float(self.second))
        self.second = self.my_text
        self.second = "0"
'''
    def dod(self):
        self.second= self.second+"+"
    def minus(self):
        self.second= self.second+"-"
    def podziel(self):
        self.second= self.second+"/"
    def multiple(self):
        self.second= self.second+"*"

    def equal_number(self):
        self.second = str(eval(self.second))
    def clear_all(self):
        self.my_text = ""
        self.second = ""
    def comma(self):
        self.second = self.second+","

    def nine(self):
        self.second= self.second+"9"
    def eight(self):
        self.second= self.second+"8"

    def seven(self):
        self.second= self.second+"7"

    def six(self):
        self.second= self.second+"6"

    def five(self):
        self.second= self.second+"5"

    def four(self):
        self.second= self.second+"4"

    def three(self):
        self.second= self.second+"3"

    def two(self):
        self.second= self.second+"2"

    def one(self):
        self.second= self.second+"1"

    def zero(self):
        self.second= self.second+"0"




class KalkulatorApp(App):
    pass

KalkulatorApp().run()