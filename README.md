# Teste de Software 
Trabalho Prático da disciplina de Teste de Software - DCC/UFMG

## Desenvolvedora:
- Selene Melo Andrade - 2019054986

## 1) Explicação do sistema

O presente sistema é uma calculadora do IRRF (Imposto de renda retido na fonte) de um indivíduo com base na passagem de diversos valores como entrada, como salário base, bônus, número de dependentes, etc. Ele possui uma interface visual em que o contribuinte entra com seu nome, CPF, informações de salário base, bonificações, periodicidade para a qual deseja calcular e eventuais descontos (dependentes, pensão alimenticia e outros). No modo "Grafico" serão entregues 3 gráficos: Um com seu salário básico e as bonificações, outro com seu salário base de cálculo e as deduções feitas para se chegar nele e o último com o valor de seu salário líquido e de seu IRRF (em reais por ano), o que forma o seu salário base para o calculo do IRRF. No modo "Relatório", o contribuinte tem um relatório com alguns dos valores totais das variáveis anteriormente referidas, além de sua aliquota efetiva de IRRF (valor do irrf/(salário base + bonificações) em porcentagem).

## 2) Tecnologias utilizadas

Para o desenvolvimento desse sistema optou-se por utilizar as seguintes tecnologias:

- **Linguagem de Programação**: Python
- **Bibliotecas**: PySimpleGUI, matplotlib, reportlab, numpy, pandas
- **Frameworks**: Unittest
- **Ferramenta de análise**: Coverage

## 3) Explicação das ferramentas utilizadas

O unittest é o framework padrão de testes unitários do Python. Ele permite criar e organizar testes para verificar o comportamento e a funcionalidade do código, garantindo sua corretude. 

O Coverage é uma ferramenta Python utilizada para medir a cobertura de testes de projetos. A cobertura de um código refere-se às partes do código que são efetivamente executados quando os testes são rodados. O uso dessa ferramenta é essencial para garantir a qualidade do software, permitindo que os desenvolvedores identifiquem facilmente trechos de códigos não testados, aumentando a confiança na robustez da aplicação e reduzindo as probabilidades do erros passarem despercebidos.
A ferramenta oferece diversas funcionalidades úteis, incluindo a medição detalhada de quais linhas ou blocos do código foram cobertos durante os testes. Além disso, ela pode gerar relatórios em diferentes formatos, como texto, HTML e XML. O relatório em HTML, por exemplo, fornece uma interface visual em que as linhas cobertas são destacadas em verde, enquanto as não cobertas aparecem em vermelho. Essa visualização facilita a análise e ajuda a priorizar áreas do código que precisam de atenção adicional. Outra vantagem é que o Coverage é compatível com diversos frameworks de teste, como unittest, pytest e nose, tornando-o versátil e fácil de integrar em diferentes projetos.

Usar o framework unittest em conjunto com o coverage permite medir a cobertura de testes do seu código. O coverage analisa quais partes do código foram executadas durante os testes, fornecendo relatórios que ajudam a identificar áreas não testadas ou insuficientemente testadas. Isso é útil para garantir que todos os casos importantes sejam validados e que o código esteja bem testado. Ao rodar o unittest com o coverage, é possível garantir uma cobertura de testes mais abrangente e melhorar a qualidade geral do software.

Por fim, integrar o Coverage em pipelines de integração contínua (CI) e entrega contínua (CD) é uma prática que visa melhorar a produtividade e a qualidade do software durante o desenvolvimento. CI/CD são práticas que automatizam o processo de integração de código e sua entrega em produção, garantindo que novas alterações no código sejam testadas e implantadas de forma rápida e eficiente. Essa integração ajuda a manter um alto nível de qualidade do código, pois permite que os desenvolvedores saibam, em tempo real, se os testes estão cobrindo todas as partes do código e se novas alterações estão sendo corretamente testadas.


## 4) Relatório de cobertura e integração CI/CD


<img width="287" alt="Captura de Tela 2024-12-15 às 23 14 07" src="https://github.com/user-attachments/assets/768ce5a2-bcd4-4ea2-8fca-2ba0ebc8d2e2" />

<img width="1280" alt="Captura de Tela 2024-12-15 às 23 14 36" src="https://github.com/user-attachments/assets/e5102e47-a200-4ccf-b8f7-77bee10179cc" />

Link do último build com sucesso do GitHub Actions:
Link do Codecov do sistema:



  



