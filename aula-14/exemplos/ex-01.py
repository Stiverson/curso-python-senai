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
menuInicial.title("Cálculo da Área do Triângulo")

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
label1.grid()
textbox1.grid()
label2.grid()
textbox2.grid()
button1.grid()
button2.grid()
labelResultado.grid()

#loop
menuInicial.mainloop()