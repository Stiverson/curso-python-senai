from tkinter import *



#funções

def calcular():
    B = float(textbox1.get())
    H = float(textbox2.get())
    A = float() 

    aux = profissao.get()

    if aux == 'h':
        A = B * H
    elif aux == 'p':
        A = (B * H ) * 1.25
    final.set("O Salário é: " + str(A))

def limpar():
    textbox1.delete(0, 'end')
    textbox2.delete(0, 'end')
    final.set(" ")

#tela
menuInicial = Tk()
menuInicial.title("Cálculo horista Professor")

#variáveis
final = StringVar()
profissao = StringVar()

#design
radio1 = Radiobutton(menuInicial, text="Horista", value='h' , variable=profissao )
radio2 = Radiobutton(menuInicial, text="Professor", value='p' , variable=profissao )

label1 = Label(menuInicial, text="Digite a quantidade de horas/aulas")
textbox1 = Entry(menuInicial)
label2 = Label(menuInicial, text="Digite o valor hora/aula")
textbox2 = Entry(menuInicial)

button1 = Button(menuInicial, text="Calcular salário bruto", command=calcular)
button2 = Button(menuInicial, text="Limpar", command=limpar)

labelResultado = Label(menuInicial, textvariable=final)

#graphs
radio1.pack()
radio2.pack()
label1.pack()
textbox1.pack()
label2.pack()
textbox2.pack()
button1.pack()
button2.pack()
labelResultado.pack()

#loop
menuInicial.mainloop()