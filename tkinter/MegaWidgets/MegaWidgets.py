import tkinter as tk
from tkinter import ttk #import to use combobox

class AboutDialog(tk.Frame):

    def __init__(self, master, version, copyRight, Contact):
        tk.Frame.__init__(self, master)
        self.pack_propagate()
        self.pack()        
        Lbl = tk.Label(self, text='%s\n%s\n%s\n'%(version, copyRight, Contact))
        Lbl.pack(expand=True, fill='both')
        BtnF = tk.Frame(self)
        BtnF.pack()
        Btn =  tk.Button(BtnF, text='Close', command=self.CloseWindow)
        Btn.pack()
        
    def CloseWindow(self):
        self.master.destroy()
class ButtonBox(tk.Frame):

    def __init__(self, master, lableOfwindow ,lableOfButton):
        self.master = master
        self.LableOfWindow = lableOfwindow
        self.master.title(self.LableOfWindow)
        self.LableOfButton = lableOfButton
        self.Frame = tk.Frame(self.master)
        self.Frame.pack()
        self.CreateButton()
        
    def CreateButton(self):
        for key in self.LableOfButton:
            Btn = tk.Button(self.Frame, text=key)
            Btn.pack(side='left', padx=5, pady=5)
            
class ListboxAndScrollBar(tk.Frame):

    def __init__(self, master):
        self.master = master
        self.master.title('List box')
        self.frame = tk.Frame(self.master)
        self.frame.pack() 
        self.Lb = tk.Listbox(self.frame)
        self.Lb.grid(row=0, column=0)
        for item in range(1,30):
            self.Lb.insert(tk.END, str(item)) 
        self.scrollBar = tk.Scrollbar(self.frame)
        self.scrollBar.grid(row=0, column=1, sticky='nsew')
        '''
        we can use widget.config(**option) to add more options that is same as
        widget.(**option)
        
        '''
        self.scrollBar.config(command=self.Lb.yview)
        self.Lb.config(yscrollcommand=self.scrollBar.set)
        
    def getvalue(self):
        a = self.Lb.curselection()
        print(a)
        for i in a:
            print(self.Lb.get(i))
class ListboxAndScrollBar_1(tk.Frame):

    def __init__(self, master):
        self.master = master
        self.master.title('List box')
        self.frame = tk.Frame(self.master)
        self.frame.pack() 
        self.Lb = tk.Listbox(self.frame)
        self.Lb.grid(row=0, column=0)
        for item in range(1,30):
            self.Lb.insert(tk.END, str(item)) 
        self.scrollBar = tk.Scrollbar(self.frame, command=self.Lb.yview)
        self.scrollBar.grid(row=0, column=1, sticky='nsew')
        '''
        we can use widget.config(**option) to add more options that is same as
        widget.(**option)
        
        '''
        self.Lb.config(yscrollcommand=self.scrollBar.set)
        
    def getvalue(self):
        a = self.Lb.curselection()
        print(a)
        for i in a:
            print(self.Lb.get(i))
        
def NewWindow(root):
    newWindow = tk.Toplevel(root)
    newWindow1 = tk.Toplevel(root)
    Version = 'Ver 1.5'
    CopyRight = 'Company CopyRight'
    Contact = 'If you have any concern, please contact me via email'
    AboutDialog(newWindow, Version, CopyRight, Contact)
    ButtonBox(newWindow1, 'Button Box', ['1','2','3'])
    
class ComboboxAndEntry(tk.Frame):

    def __init__(self, master):
        self.master = root
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.Combobox()
        
    def Combobox(self):
        self.stringvar = tk.StringVar()
        self.display = tk.Entry(self.master, textvariable=self.stringvar)
        self.display.pack()
        self.comboBox = ttk.Combobox(self.master, values=['a','b','c','d'], 
                                     textvariable=self.stringvar)
        self.comboBox.current(0)
        self.comboBox.pack()
        
    def getValue(self):
        print(self.comboBox.get())
        
root = tk.Tk()
LB = ListboxAndScrollBar_1(root)
But = tk.Button(root, text='New Window', command=LB.getvalue)
But.pack()
root.mainloop()
