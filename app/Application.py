from Usuarios import Usuarios
from tkinter import *

class Application:
    def __init__(self, master= None):
        self.fonte = ("Verdana", "10")
        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack() 
        
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        
        
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "16", "bold")
        self.titulo.pack()