
class LogicaCalculadora:

    def __init__(self, salario_base, bonus_tempo, bonus_formacao, bonus_periculosidade,
            mes_inicio,ano_inicio,mes_fim,ano_fim,
            numero_dependentes,pensao_alimenticia,outros_descontos,tipooferta):

        self.salario_base                  = salario_base
        self.bonus_tempo                   = bonus_tempo
        self.bonus_formacao                = bonus_formacao
        self.bonus_periculosidade          = bonus_periculosidade
        self.salario_bruto                 = 0
        self.bonus                         = 0
        self.desconto_inss                 = 0
        self.desconto_dependente           = 0

        self.mes_inicio             = mes_inicio
        self.ano_inicio             = ano_inicio
        self.mes_fim                = mes_fim
        self.ano_fim                = ano_fim
        self.anos_vigencia_aux      = self.ano_fim - self.ano_inicio + 1

        self.numero_dependentes     = numero_dependentes
        self.pensao_alimenticia     = pensao_alimenticia
        self.outros_descontos       = outros_descontos
        self.tipooferta             = tipooferta

        self.salario_base_de_calculo = 0
        self.salario_liquido        = 0
        self.anos_vigencia            = None
        self.irrf_recolhido = 0
        self.total_deducoes = None  #Linha adicionada
        self.aliquota_ = None  #Linha adicionada

    #def calculo_bonus_e_salario_bruto(self):

       # self.bonus = self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade

        #self.salario_bruto = self.salario_base + self.bonus
        
    def calculo_bonus_e_salario_bruto(self):
        # Validação do tipo de oferta
        if self.tipooferta not in ['CLT', 'Outros tipos permitidos']:  # Adicione os tipos válidos
            raise ValueError(f"Tipo de oferta inválido: {self.tipooferta}")

        # Calculando bônus e protegendo contra valores negativos
        self.bonus = max(0, self.bonus_tempo) + max(0, self.bonus_formacao) + max(0, self.bonus_periculosidade)

        # Calculando o salário bruto
        self.salario_bruto = self.salario_base + self.bonus

    def calculo_deducoes_e_salario_base(self):

        if (self.salario_bruto <= 1320.00):
            self.desconto_inss = self.salario_bruto * 0.075

        elif (1320.01 <= self.salario_bruto <= 2571.29):
            self.desconto_inss = ((self.salario_bruto - 1320.01) * 0.09) + 99.00

        elif (2571.30 <= self.salario_bruto <= 3856.94):
            self.desconto_inss = ((self.salario_bruto - 2571.30) * 0.12) + 112.62 + 99.00

        elif (3856.95 <= self.salario_bruto <= 7507.49):
            self.desconto_inss = ((self.salario_bruto - 3856.95) * 0.14) + 154.28 + 112.62 + 99.00

        else:
            self.desconto_inss = 876.97

        self.desconto_dependente = self.numero_dependentes * 189.59

        self.total_deducoes = self.desconto_inss + self.desconto_dependente + self.pensao_alimenticia + self.outros_descontos

        self.salario_base_de_calculo = self.salario_bruto - self.total_deducoes

    #def calculo_irrf_recolhido_salario_liquido_aliquota(self):

    #    if (self.salario_base_de_calculo <= 2112.00):
     #       self.irrf_recolhido = 0

      #  elif (2112.01 <= self.salario_base_de_calculo <= 2826.65):
       #     self.irrf_recolhido = ((self.salario_base_de_calculo - 2112.01) * 0.075)

        #elif (2826.66 <= self.salario_base_de_calculo <= 3751.05):
          #  self.irrf_recolhido = ((self.salario_base_de_calculo - 2826.66) * 0.15) + 53.60

        #elif (3751.06 <= self.salario_base_de_calculo <= 4664.68):
         #   self.irrf_recolhido = ((self.salario_base_de_calculo - 3751.06) * 0.225) + 138.66 + 53.60

        #elif (self.salario_base_de_calculo > 4664.68):
         #   self.irrf_recolhido = ((self.salario_base_de_calculo - 4664.68) * 0.275) + 205.56 + 138.66 + 53.60

        #self.salario_liquido = self.salario_base_de_calculo - self.irrf_recolhido

        #self.aliquota_ = self.irrf_recolhido/self.salario_bruto

    def calculo_irrf_recolhido_salario_liquido_aliquota(self):
        # Proteção contra salário bruto ou base de cálculo inválidos
        if self.salario_base_de_calculo <= 0 or self.salario_bruto <= 0:
            self.irrf_recolhido = 0
            self.salario_liquido = 0
            self.aliquota_ = 0
            return

        # Faixas de cálculo do IRRF com alíquotas e deduções fixas
        if self.salario_base_de_calculo <= 2112.00:
            self.irrf_recolhido = 0

        elif 2112.01 <= self.salario_base_de_calculo <= 2826.65:
            self.irrf_recolhido = ((self.salario_base_de_calculo - 2112.01) * 0.075)

        elif 2826.66 <= self.salario_base_de_calculo <= 3751.05:
            self.irrf_recolhido = ((self.salario_base_de_calculo - 2826.66) * 0.15) + 53.60

        elif 3751.06 <= self.salario_base_de_calculo <= 4664.68:
            self.irrf_recolhido = ((self.salario_base_de_calculo - 3751.06) * 0.225) + 138.66 + 53.60

        elif self.salario_base_de_calculo > 4664.68:
            self.irrf_recolhido = ((self.salario_base_de_calculo - 4664.68) * 0.275) + 205.56 + 138.66 + 53.60

        # Cálculo do salário líquido
        self.salario_liquido = self.salario_base_de_calculo - self.irrf_recolhido

        # Proteção adicional para evitar divisão por zero
        if self.salario_bruto > 0:
            self.aliquota_ = self.irrf_recolhido / self.salario_bruto
        else:
            self.aliquota_ = 0

    #def definir_anos_vigencia(self):

     #   aux = self.ano_fim - self.ano_inicio + 1

      #  self.anos_vigencia = list(range(aux))

       # for i in range(0, aux, 1):
        #    self.anos_vigencia[i] = str(self.ano_inicio + i)

    def definir_anos_vigencia(self):
        # Validação do período: o início não pode ser posterior ao fim
        if (self.ano_inicio > self.ano_fim) or (self.ano_inicio == self.ano_fim and self.mes_inicio > self.mes_fim):
            raise ValueError("O período especificado é inválido: o início é posterior ao fim.")

        # Geração da lista de anos de vigência
        self.anos_vigencia = [str(ano) for ano in range(self.ano_inicio, self.ano_fim + 1)]

    def preparar_graficos(self, salario_liquido, irrf_recolhido, salario_base, adicoes, salario_base_de_calculo, total_deducoes):
    
        salario_liquido_list         = list(range(self.anos_vigencia_aux))
        irrf_recolhido_list          = list(range(self.anos_vigencia_aux))
        salario_base_list            = list(range(self.anos_vigencia_aux))
        adicoes_list                 = list(range(self.anos_vigencia_aux))
        salario_base_de_calculo_list = list(range(self.anos_vigencia_aux))
        total_deducoes_list          = list(range(self.anos_vigencia_aux))

        self.total_deducoes = None  #Adicionado
        self.aliquota_ = None  #Adicionado


        if(self.anos_vigencia_aux == 1):

            salario_liquido_list[0]         = salario_liquido         * (self.mes_fim - self.mes_inicio + 1)
            irrf_recolhido_list[0]          = irrf_recolhido          * (self.mes_fim - self.mes_inicio + 1)
            salario_base_list[0]            = salario_base            * (self.mes_fim - self.mes_inicio + 1)
            adicoes_list[0]                 = adicoes                 * (self.mes_fim - self.mes_inicio + 1)
            salario_base_de_calculo_list[0] = salario_base_de_calculo * (self.mes_fim - self.mes_inicio + 1)
            total_deducoes_list[0]          = total_deducoes          * (self.mes_fim - self.mes_inicio + 1)

        elif(self.anos_vigencia_aux > 1):

            salario_liquido_list[0]         = salario_liquido         * (12 - self.mes_inicio + 1)
            irrf_recolhido_list[0]          = irrf_recolhido          * (12 - self.mes_inicio + 1)
            salario_base_list[0]            = salario_base            * (12 - self.mes_inicio + 1)
            adicoes_list[0]                 = adicoes                 * (12 - self.mes_inicio + 1)
            salario_base_de_calculo_list[0] = salario_base_de_calculo * (12 - self.mes_inicio + 1)
            total_deducoes_list[0]          = total_deducoes          * (12 - self.mes_inicio + 1)

            for i in range(1, (self.anos_vigencia_aux - 1), 1):

                salario_liquido_list[i]         = salario_liquido         * 12
                irrf_recolhido_list[i]          = irrf_recolhido          * 12
                salario_base_list[i]            = salario_base            * 12
                adicoes_list[i]                 = adicoes                 * 12
                salario_base_de_calculo_list[i] = salario_base_de_calculo * 12
                total_deducoes_list[i]          = total_deducoes          * 12

            salario_liquido_list[self.anos_vigencia_aux - 1]         = salario_liquido         * self.mes_fim
            irrf_recolhido_list[self.anos_vigencia_aux - 1]          = irrf_recolhido          * self.mes_fim
            salario_base_list[self.anos_vigencia_aux - 1]            = salario_base            * self.mes_fim
            adicoes_list[self.anos_vigencia_aux - 1]                 = adicoes                 * self.mes_fim
            salario_base_de_calculo_list[self.anos_vigencia_aux - 1] = salario_base_de_calculo * self.mes_fim
            total_deducoes_list[self.anos_vigencia_aux - 1]          = total_deducoes          * self.mes_fim

        return salario_liquido_list, irrf_recolhido_list, salario_base_list, adicoes_list, salario_base_de_calculo_list, total_deducoes_list
    
    def preparar_relatorio(self, salario_base, salario_bruto, salario_base_de_calculo, salario_liquido, irrf_recolhido):
    
        if(self.anos_vigencia_aux == 1):

            salario_base = salario_base * (self.mes_fim - self.mes_inicio + 1)
            salario_bruto = salario_bruto * (self.mes_fim - self.mes_inicio + 1) 
            salario_base_de_calculo = salario_base_de_calculo * (self.mes_fim - self.mes_inicio + 1)
            salario_liquido = salario_liquido * (self.mes_fim - self.mes_inicio + 1)
            irrf_recolhido  = irrf_recolhido * (self.mes_fim - self.mes_inicio + 1)
            aliquota_ = irrf_recolhido/salario_bruto

        elif(self.anos_vigencia_aux > 1):

            salario_base = salario_base * ((12 - self.mes_inicio + 1) + ((self.anos_vigencia_aux - 2) * 12) + (self.mes_fim))
            salario_bruto = salario_bruto * ((12 - self.mes_inicio + 1) + ((self.anos_vigencia_aux - 2) * 12) + (self.mes_fim))
            salario_base_de_calculo = salario_base_de_calculo * ((12 - self.mes_inicio + 1) + ((self.anos_vigencia_aux - 2) * 12) + (self.mes_fim))
            salario_liquido = salario_liquido * ((12 - self.mes_inicio + 1) + ((self.anos_vigencia_aux - 2) * 12) + (self.mes_fim))
            irrf_recolhido  = irrf_recolhido * ((12 - self.mes_inicio + 1) + ((self.anos_vigencia_aux - 2) * 12) + (self.mes_fim))
            aliquota_ = irrf_recolhido/salario_bruto

        return salario_base, salario_bruto, salario_base_de_calculo, salario_liquido, irrf_recolhido, aliquota_

    def enviardadosparagrafico(self):

        return self.salario_liquido, self.irrf_recolhido, self.anos_vigencia, self.salario_base, (self.bonus_tempo + self.bonus_formacao + self.bonus_periculosidade), self.salario_base_de_calculo, self.total_deducoes

    def enviardadospararelatorio(self):

        return self.salario_base, self.salario_bruto, self.salario_base_de_calculo, self.anos_vigencia, self.salario_liquido, self.irrf_recolhido, self.aliquota_
