# Sistema de Avaliação de Risco de Falha em Motores Elétricos

![Fuzzy Logic](https://img.shields.io/badge/Fuzzy-Logic-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)

## Descrição

Sistema especialista baseado em **lógica fuzzy** para avaliação do risco de falha em motores elétricos industriais, analisando cinco parâmetros críticos:

1. Resistência de isolamento elétrico
2. Tensão de alimentação
3. Presença de folgas mecânicas
4. Temperatura ambiente
5. Tempo de operação contínua

## Funcionalidades

- Interface interativa para entrada de parâmetros
- Visualização dos conjuntos fuzzy e graus de pertinência
- Cálculo automático do risco de falha (0-100%)
- Exibição gráfica dos resultados

  ## Exibição Gráfica

## Tecnologias Utilizadas

-Risco baixo
![Imagem1](https://github.com/user-attachments/assets/32662013-1f19-4241-b366-1f98a7b2799d)

-Risco médio
![Imagem2](https://github.com/user-attachments/assets/c37876f6-f52a-40ce-96a6-b1440d3f641c)

-Risco alto
![Imagem3](https://github.com/user-attachments/assets/1ecb97de-85f6-4091-a8a6-ddfa011961b5)

| Tecnologia | Versão |
|------------|--------|
| ![Python](https://img.shields.io/badge/Python-3.x-blue) | 3.x |
| ![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-0.5.0-orange) | 0.5.0 |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.3-red) | 3.10.3 |
| ![NumPy](https://img.shields.io/badge/NumPy-2.2.6-yellow) | 2.2.6 |
| ![SciPy](https://img.shields.io/badge/SciPy-1.15.3-blueviolet) | 1.15.3 |
| ![NetworkX](https://img.shields.io/badge/NetworkX-3.5-green) | 3.5 |

## Aplicações

- Manutenção preditiva
- Monitoramento operacional
- Planejamento de manutenção
- Redução de falhas inesperadas

## Como Executar

```bash
# 1. Instalar dependências (recomendado usar ambiente virtual)
pip install -r requirements.txt

# 2. Executar o sistema
python sistema_risco_falha.py
