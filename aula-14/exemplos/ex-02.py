from tkinter import *

#Calcular a area de um triangulo. A = (b * h) / 2

#funções
def calcular():
    B = float(textbox1.get())
    H = float(textbox2.get())
    A = (B * H) / 2
    final.set("A área é: " + str(A))

def limpar():
    textbox1.delete(0, 'end')
    textbox2.delete(0, 'end')

#tela
menuInicial = Tk()
menuInicial.title("Cálculo da Área do Trângulo")

#variáveis
final = StringVar()

#design
label1 = Label(menuInicial, text="Insira a Base: ")
textbox1 = Entry(menuInicial)
label2 = Label(menuInicial, text="Insira a Altura: ")
textbox2 = Entry(menuInicial)
button1 = Button(menuInicial, text="Calcular", command=calcular)
button2 = Button(menuInicial, text="Limpar", command=limpar)
labelResultado = Label(menuInicial, textvariable=final)

#graphs
label1.grid(row=0, column=0)
textbox1.grid(row=0, column=1)
label2.grid(row=1, column=0)
textbox2.grid(row=1, column=1)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
labelResultado.grid(row=3, column=0, columnspan=2)

#loop
menuInicial.mainloop()