# GUI mit tkinter

from tkinter import *
 
class App: 
  def __init__(self):
    fenster = Tk()
    fenster.title("tkinter Demo")
 
    button = Button(fenster, text="OK", 
                    command=self.button_click)
    button.pack()
 
    self.entry = Entry(fenster)
    self.entry.insert(0, "Name")
    self.entry.pack()
 
    self.lbl = Label(fenster, 
                     text="Name eingeben")
    self.lbl.pack()
 
    fenster.mainloop()
 
  def button_click(self):
    eingabe = self.entry.get()
    self.lbl.configure(text="Hallo " + eingabe)

app = App()
