# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:01:36 2017

@author: PCN1HC
"""
import tkinter as tk

def add(a,b):
    c = a + b
    return c
def sub(a, b):
    c = a - b
    return c
def mul(a, b):
    c = float(a*b)
    return c
def div(a, b):
    c = float(a/b)
    return c
optr = {'+':add, '-':sub, '*':mul, '/':div}
def frame(root, side):
    w = tk.Frame(root)
    w.pack(side = side, expand="YES",fill= "both")
    return w
def button(root,side, text, command =None):
    w = tk.Button(root, text=text, command=command)
    w.pack(side=side,expand="YES",fill= "both")
    return w  
class Application(tk.Frame):
    
    def __init__(self , master = None):
        super().__init__(master)
        self.config(width=200, height=200)
        self.pack_propagate(0)
        self.pack(expand="YES", fill="both")    
        master.title("Calculator")
        self.create_widgets()
        # Define variable to use
        self.Number = [['',0],['',0]]       
        self.temp = 0
    def create_widgets(self):
        # Entry to display all buuton is pressed, 
        # only delete when  pressing '=' button
        self.display2 = tk.StringVar()
        # Entry to display first and second number and result
        self.display = tk.StringVar()
        tk.Entry(self, relief=tk.SOLID, textvariable=self.display2
                 ).pack(side="top", expand="YES",fill="both")
        tk.Entry(self, relief=tk.SOLID, textvariable=self.display
                 ).pack(side="top", expand="YES",fill="both")
        # Create buttons
        for key in ("123","456","789","-0."):
            keyF = frame(self, "top")
            for char in key:
                button(keyF,"left",char, lambda char=char: self.PressNumberButton(char))
        keyC = frame(self, 'top')
        for cal in ('+-*/='):
            button(keyC, 'left', cal, lambda cal=cal: self.PressOperatorButton(cal))
        clearF = frame(self, 'top')
        # Button clear all
        button(clearF, 'left', 'Clear', self.PressButtonClearAll)
        # Button clear what is entered
        button(clearF, 'left', 'Clear Entry', self.PressButtonClearEntry)
        # Button clear the last character is entered
        button(clearF, 'left', '←', self.PressButtonArrow)
    def PressNumberButton(self, char):
        #Check if first numbet is entered
        if self.Number[0][1] != 0:
            # If first number is entered, delete the entry 
            self.display.set('')
            # Save the first number is entered to temp variable
            # and set the first number is zero to enter the second number
            self.temp = self.Number[0][1]
            self.Number[0][1] = 0
        # Enter the first and second number, if first and second number are zero
        # The second number is entered when save the first number then set first 
        # number is zero       
        self.display.set(self.display.get() + char)

    def PressOperatorButton(self, cal):
        # Assign tempory variable to the first number 
        self.Number[0][1] = self.temp        
        if ((self.display.get() != '') and (float(self.display.get()) != 0)):
            # Check if entered value is not empty or zero, pressing operator button is ok
            if cal == '=':
                # Check if press the '=' button, calculate and display result
                if self.Number[0][1] != 0:
                    # Check first number is not zero, calculate and display result
                    self.Number[1][1] = self.display.get()
                    result = self.Calculate()
                    self.ClearNumber()
                    
                else:
                    # Display what is entered
                    result = self.display.get()
                self.display.set(result)
                self.display2.set(result)
                self.temp = 0                
            else:
                # press thoes operator button such as +-*/, save number is entered, operator
                # and calculate
                if self.Number[0][1] != 0:   
                    # Check if the first number is not zero, save entered value
                    # and pressed operator for the next calculation
                    # Calculation and display the result
                    # Save result to first number, 0 to second number
                    self.display2.set(self.display2.get() + 
                                      self.display.get() + cal)
                    self.Number[1]= [cal, self.display.get()]
                    result = self.Calculate()
                    self.display.set(result)
                    self.Number[0] = [self.Number[1][0], result]
                    self.Number[1] = ['',0]
                else:
                    # Save entered value to first number 
                    # and entered operator for the next calculation
                    self.display2.set(self.display.get() + cal)
                    self.Number[0]= [cal, self.display.get()]

    def Calculate(self):
        result = optr[(self.Number[0][0])](float(self.Number[0][1]),
                     float(self.Number[1][1]))
        return result 
    
    def ClearNumber(self):
        self.Number = [['',0],['',0]]
    # clear what is entered        
    def PressButtonClearEntry(self):
        self.display.set('')
    # clear all
    def PressButtonClearAll(self):
        self.ClearNumber()
        self.display.set('')
        self.display2.set('')
    #  clear the last character is entered    
    def PressButtonArrow(self):
        entry = self.display.get()        
        entry = entry[:(len(entry)-1)]
        self.display.set(entry)

        
root = tk.Tk()
app = Application(root)
root.mainloop()
