# Teste de Softawe 
Trabalho Prático da disciplina de Teste de Software - DCC/UFMG

## Integrante
- Selene Melo Andrade - 2019054986

## 1) Explicação do sistema

O presente sistema é uma calculadora do IRRF (Imposto de renda retido na fonte) de um indivíduo com base na passagem de diversos valores como entrada, como salário base, bônus, número de dependentes, etc. Ele possui uma interface visual em que o contribuinte entra com seu nome, CPF, informações de salário base, bonificações, periodicidade para a qual deseja calcular e eventuais descontos (dependentes, pensão alimenticia e outros). No modo "Grafico" serão entregues 3 gráficos: Um com seu salário básico e as bonificações, outro com seu salário base de cálculo e as deduções feitas para se chegar nele e o último com o valor de seu salário líquido e de seu IRRF (em reais por ano), o que forma o seu salário base para o calculo do IRRF. No modo "Relatório", o contribuinte tem um relatório com alguns dos valores totais das variáveis anteriormente referidas, além de sua aliquota efetiva de IRRF (valor do irrf/(salário base + bonificações) em porcentagem).

## 2) Tecnologias utilizadas

Para o desenvolvimento desse sistema optou-se por utilizar as seguintes tecnologias:

- **Linguagem de Programação**: Python
- **Bibliotecas**: PySimpleGUI, matplotlib, reportlab, numpy, pandas
- **Frameworks**: Pytest
- **Ferramenta de análise**: Coverage

## 3) Explicação das ferramentas utilizadas

O Coverage é uma ferramenta Python utilizada para medir a cobertura de testes de projetos. A cobertura de um código refere-se às partes do código que são efetivamente executados quando os testes são rodados. O uso dessa ferramenta é essencial para garantir a qualidade do software, permitindo que os desenvolvedores identifiquem facilmente trechos de códigos não testados, aumentando a confiança na robustez da aplicação e reduzindo as probabilidades do erros passarem despercebidos.
A ferramenta oferece diversas funcionalidades úteis, incluindo a medição detalhada de quais linhas ou blocos do código foram cobertos durante os testes. Além disso, ela pode gerar relatórios em diferentes formatos, como texto, HTML e XML. O relatório em HTML, por exemplo, fornece uma interface visual em que as linhas cobertas são destacadas em verde, enquanto as não cobertas aparecem em vermelho. Essa visualização facilita a análise e ajuda a priorizar áreas do código que precisam de atenção adicional. Outra vantagem é que o Coverage é compatível com diversos frameworks de teste, como unittest, pytest e nose, tornando-o versátil e fácil de integrar em diferentes projetos.

Para melhorar a produtividade, é possível integrar o Coverage em pipelines de integração contínua (CI/CD), monitorando a cobertura de testes em cada alteração do código, como faremos a seguir.


## 4) Relatório de cobertura

- Relátorio impresso na saída do terminal
  
<img width="493" alt="Captura de Tela 2024-12-15 às 15 09 16" src="https://github.com/user-attachments/assets/670ac1cd-f5c8-4bc6-8265-21ea05987523" />

- Relatório html

<img width="557" alt="Captura de Tela 2024-12-15 às 15 10 55" src="https://github.com/user-attachments/assets/ec05c038-e3b7-4be4-9e1c-344ce5221aa9" />
<img width="821" alt="Captura de Tela 2024-12-15 às 15 11 12" src="https://github.com/user-attachments/assets/a8176763-7619-4283-9d06-3babbbb124a6" />
<img width="1063" alt="Captura de Tela 2024-12-15 às 15 11 05" src="https://github.com/user-attachments/assets/7a998a26-e8ac-4214-b768-4a626219b19d" />


  



