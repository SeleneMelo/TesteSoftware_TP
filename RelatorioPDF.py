from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor

class RelatorioPDF:

    def __init__(self, salario_base, salario_bruto, salario_base_de_calculo,
                anos_vigencia,
                salario_liquido, irrf_recolhido, aliquota,
                nome_contribuinte, cpf_contribuinte):

        self.salario_base = salario_base
        self.salario_bruto = salario_bruto
        self.salario_base_de_calculo = salario_base_de_calculo

        self.anos_vigencia            = anos_vigencia
        
        self.salario_liquido        = salario_liquido
        self.irrf_recolhido     = irrf_recolhido
        self.aliquota = aliquota
        
        self.nome_contribuinte                   = nome_contribuinte
        self.cpf_contribuinte                   =  cpf_contribuinte

    def gerarrelatorio(self):

        c = canvas.Canvas("Relatório de desconto de " + str(self.nome_contribuinte) + ".pdf", pagesize=(160*mm,160*mm))

        pc = list(range(2))

        anos_vigencia_aux = len(self.anos_vigencia)
        
        pc[0] = self.anos_vigencia[0]
        pc[1] = self.anos_vigencia[anos_vigencia_aux - 1]

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,300,"Bem vindo contribuinte " + self.nome_contribuinte + ".")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,280,"Portador do CPF " + self.cpf_contribuinte + ".")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,200,"Seu salário base é de " + str(round(self.salario_base, 2)) + " reais.")
        c.setFillColor(HexColor('#158d74'))
        c.setFont("Helvetica", 13)
        c.drawString(15,100,"Seu salário bruto, pós adição de bonificações é " + str(round(self.salario_bruto, 2)) + " reais.")
        c.showPage()

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,300,"A periodicidade começou em " + str(pc[0]) + ".")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,150,"A periodicidade terminou em " + str(pc[1]) + ".")
        c.showPage()

        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,300, "Seu salário líquido pós IRRF é de " + str(round(self.salario_liquido, 2)) + " reais.")
        c.setFillColor(HexColor('#148c73'))
        c.setFont("Helvetica", 13)
        c.drawString(15,200,"Seu IRRF ficou em " + str(round(self.irrf_recolhido,2)) + " reais.")
        c.setFillColor(HexColor('#158d74'))
        c.setFont("Helvetica", 13)
        c.drawString(15,100,"A aliquota efetiva ficou em " + str(round(self.aliquota * 100, 2)) + "%.")
        c.showPage()

        c.save()
