# Sistema de Avaliação de Risco de Falha em Motores Elétricos 🔧⚡

![Fuzzy Logic](https://img.shields.io/badge/Fuzzy-Logic-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)

## 📌 Descrição

Sistema especialista baseado em **lógica fuzzy** para avaliação do risco de falha em motores elétricos industriais, analisando cinco parâmetros críticos:

1. 🔌 Resistência de isolamento elétrico
2. ⚡ Tensão de alimentação
3. 🛠️ Presença de folgas mecânicas
4. 🌡️ Temperatura ambiente
5. ⏱️ Tempo de operação contínua

## 🚀 Funcionalidades

- 🖥️ Interface interativa para entrada de parâmetros
- 📊 Visualização dos conjuntos fuzzy e graus de pertinência
- 🧮 Cálculo automático do risco de falha (0-100%)
- 📈 Exibição gráfica dos resultados

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/Python-3.x-blue) | Linguagem principal |
| ![skfuzzy](https://img.shields.io/badge/skfuzzy-0.9.0-orange) | Lógica fuzzy |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-red) | Visualização |
| ![NumPy](https://img.shields.io/badge/NumPy-1.21.0-yellow) | Cálculos numéricos |

## 💡 Aplicações

- ✅ Manutenção preditiva
- ✅ Monitoramento operacional
- ✅ Planejamento de manutenção
- ✅ Redução de falhas inesperadas

## ⚙️ Como Executar

```bash
# 1. Instalar dependências
pip install numpy scikit-fuzzy matplotlib

# 2. Executar o sistema
python sistema_risco_falha.py
