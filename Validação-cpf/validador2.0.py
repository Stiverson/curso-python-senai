import tkinter as tk

def valida_cpf(cpf):
    
  def verificar_cpf():
    
   cpf = entry_cpf.get()
     if valida_cpf(cpf):
        resultado.config(text="CPF válido")
     else:
        resultado.config(text="CPF inválido")

janela = tk.Tk()
janela.title("Validador de CPF")


label_cpf = tk.Label(janela, text="Digite o CPF:")
entry_cpf = tk.Entry(janela)
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_cpf)
resultado = tk.Label(janela, text="")


label_cpf.pack()
entry_cpf.pack()
botao_verificar.pack()
resultado.pack()

janela.mainloop()