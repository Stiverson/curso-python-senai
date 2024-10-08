from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado para Conclusão:")

valor_total = int(horas_estimadas) * int(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template_senai_v.png", x=0, y=0)

pdf.text(120, 165, projeto)
pdf.text(120, 180, horas_estimadas)
pdf.text(120, 196, valor_hora)
pdf.text(120, 212, prazo)
pdf.text(120, 228, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!!!!")
