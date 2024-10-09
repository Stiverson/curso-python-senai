from tkinter import *

raiz = Tk()

container1 = Frame(raiz)
container1.pack()
botao = Button(container1)
botao["text"] = "Senai"
botao["background"] = "blue"
botao.pack()
raiz.mainloop()