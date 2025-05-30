# Bibliotecas
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


resistencia_isolamento_eletrico = ctrl.Antecedent(np.arange(0, 1001, 1), 'resistencia_isolamento_eletrico') # trapézio resistência (Ohms)
tensao_alimentacao = ctrl.Antecedent(np.arange(198, 243, 1), 'tensao_alimentacao') # triângulo (V) tolerancia 10% do valor nominal pag 13
presenca_folgas_mecanicas = ctrl.Antecedent(np.arange(0, 0.31, 0.01), 'presenca_folgas_mecanicas') # trapézio 3 regras baixo, media e alto folga (radial) (mm)
temperatura_ambiente = ctrl.Antecedent(np.arange(-20, 41, 1), 'temperatura_ambiente') # trapézio (C)
tempo_operacao_continua = ctrl.Antecedent(np.arange(0, 361, 1), 'tempo_operacao_continua') # trapézio (360 horas ou 15 dias)

risco_falha = ctrl.Consequent(np.arange(0, 101, 1), 'risco_falha') # triângulo

# Resistência de isolamento elétrico (Ohms) — Universo: 0 a 1000
resistencia_isolamento_eletrico['baixo'] = fuzz.trapmf(resistencia_isolamento_eletrico.universe, [0, 0, 100, 300])
resistencia_isolamento_eletrico['normal'] = fuzz.trapmf(resistencia_isolamento_eletrico.universe, [200, 400, 600, 700])
resistencia_isolamento_eletrico['alto'] = fuzz.trapmf(resistencia_isolamento_eletrico.universe, [650, 800, 1000, 1000])

# Tensão de alimentação (V) — Universo: 0 a 242
tensao_alimentacao['baixo'] = fuzz.trimf(tensao_alimentacao.universe, [198, 198, 200])
tensao_alimentacao['normal'] = fuzz.trimf(tensao_alimentacao.universe, [198, 220, 242])
tensao_alimentacao['alto'] = fuzz.trimf(tensao_alimentacao.universe, [240, 242, 242])

# Folga mecânica radial (mm) — Universo: 0 a 0.30
presenca_folgas_mecanicas['baixo'] = fuzz.trapmf(presenca_folgas_mecanicas.universe, [0.00, 0.00, 0.05, 0.10])
presenca_folgas_mecanicas['normal'] = fuzz.trapmf(presenca_folgas_mecanicas.universe, [0.08, 0.12, 0.18, 0.22])
presenca_folgas_mecanicas['alto'] = fuzz.trapmf(presenca_folgas_mecanicas.universe, [0.20, 0.25, 0.30, 0.30])

# Temperatura ambiente (ºC) — Universo: -20 a 40
temperatura_ambiente['baixo'] = fuzz.trapmf(temperatura_ambiente.universe, [-20, -20, 0, 10])
temperatura_ambiente['normal'] = fuzz.trapmf(temperatura_ambiente.universe, [5, 15, 25, 30])
temperatura_ambiente['alto'] = fuzz.trapmf(temperatura_ambiente.universe, [28, 33, 40, 40])

# Tempo de operação contínua (h) — Universo: 0 a 360
tempo_operacao_continua['curto'] = fuzz.trapmf(tempo_operacao_continua.universe, [0, 0, 60, 120])
tempo_operacao_continua['medio'] = fuzz.trapmf(tempo_operacao_continua.universe, [100, 160, 240, 300])
tempo_operacao_continua['longo'] = fuzz.trapmf(tempo_operacao_continua.universe, [280, 320, 360, 360])

# Risco de falha (%) — Universo: 0 a 100
risco_falha['baixo'] = fuzz.trimf(risco_falha.universe, [0, 20, 40])
risco_falha['medio'] = fuzz.trimf(risco_falha.universe, [30, 50, 70])
risco_falha['alto'] = fuzz.trimf(risco_falha.universe, [60, 80, 100])

rules = [
    # cenário ideal: tempo curto medio e longo
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['normal'] & tempo_operacao_continua['curto'], risco_falha['baixo']),
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['normal'] & tempo_operacao_continua['medio'], risco_falha['baixo']),
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['normal'] & tempo_operacao_continua['longo'], risco_falha['medio']),
    
    # alternando diferentes variáveis
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['curto'], risco_falha['baixo']),
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['alto'] & tempo_operacao_continua['curto'], risco_falha['baixo']),
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['normal'] & tempo_operacao_continua['curto'], risco_falha['baixo']),
    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['normal'] & tempo_operacao_continua['curto'], risco_falha['baixo']),

    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['medio'], risco_falha['medio']),
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['alto'] & tempo_operacao_continua['medio'], risco_falha['medio']),
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['normal'] & tempo_operacao_continua['medio'], risco_falha['medio']),
    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['normal'] & tempo_operacao_continua['medio'], risco_falha['medio']),

    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['longo'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['normal'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['normal'] & temperatura_ambiente['alto'] & tempo_operacao_continua['longo'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['normal'] & tempo_operacao_continua['longo'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['normal'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['normal'] & tempo_operacao_continua['longo'], risco_falha['alto']),

    # cenário dos 2 extremos: tempo curto medio e longo
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['curto'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['medio'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['baixo'] & tensao_alimentacao['baixo'] & presenca_folgas_mecanicas['baixo'] & temperatura_ambiente['baixo'] & tempo_operacao_continua['longo'], risco_falha['alto']),

    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['alto'] & tempo_operacao_continua['curto'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['alto'] & tempo_operacao_continua['medio'], risco_falha['alto']),
    ctrl.Rule(resistencia_isolamento_eletrico['alto'] & tensao_alimentacao['alto'] & presenca_folgas_mecanicas['alto'] & temperatura_ambiente['alto'] & tempo_operacao_continua['longo'], risco_falha['alto']),
]

# Sistema de controle
risco_ctrl = ctrl.ControlSystem(rules)
simulador = ctrl.ControlSystemSimulation(risco_ctrl)

# Função de interação]
def regras_ativas_motor():
  # Entradas manuais
  resistencia_isolamento_eletrico_input = float(input("Resistência de Isolamento Elétrico (0 a 1000 MΩ): "))
  tensao_alimentacao_input = float(input("Tensão de Alimentação (198 a 242 V): "))
  presenca_folgas_mecanicas_input = float(input("Presença de Folgas Mecânicas (0.00 a 0.30 mm): "))
  temperatura_ambiente_input = float(input("Temperatura Ambiente (-20 a 40 ºC): "))
  tempo_operacao_continua_input = float(input("Tempo de Operação Contínua (0 a 360 h): "))

  # Validação
  if not (0 <= resistencia_isolamento_eletrico_input <= 1000 and
          0 <= tensao_alimentacao_input <= 242 and
          0 <= presenca_folgas_mecanicas_input <= 0.30 and
          -20 <= temperatura_ambiente_input <= 40 and
          0 <= tempo_operacao_continua_input <= 360):
      print("Um ou mais valores estão fora dos limites permitidos.")
      return

  # Mostrar valores informados
  print(f"\nEntradas:")
  print(f"Resistência de Isolamento Elétrico: {resistencia_isolamento_eletrico_input} MΩ")
  print(f"Tensão de Alimentação: {tensao_alimentacao_input} V")
  print(f"Presença de Folgas Mecânicas: {presenca_folgas_mecanicas_input} mm")
  print(f"Temperatura Ambiente: {temperatura_ambiente_input} ºC")
  print(f"Tempo de Operação Contínua: {tempo_operacao_continua_input} h")

  # Graus de pertinência
  print("\nGraus de pertinência (ativação dos conjuntos fuzzy):")

  print("→ Resistência de Isolamento Elétrico:")
  for termo in resistencia_isolamento_eletrico.terms:
      grau = fuzz.interp_membership(
          resistencia_isolamento_eletrico.universe,
          resistencia_isolamento_eletrico[termo].mf,
          resistencia_isolamento_eletrico_input
      )
      if grau > 0:
          print(f"   - {termo}: {grau:.2%}")

  print("→ Tensão de Alimentação:")
  for termo in tensao_alimentacao.terms:
      grau = fuzz.interp_membership(
          tensao_alimentacao.universe,
          tensao_alimentacao[termo].mf,
          tensao_alimentacao_input
      )
      if grau > 0:
          print(f"   - {termo}: {grau:.2%}")

  print("→ Presença de Folgas Mecânicas:")
  for termo in presenca_folgas_mecanicas.terms:
      grau = fuzz.interp_membership(
          presenca_folgas_mecanicas.universe,
          presenca_folgas_mecanicas[termo].mf,
          presenca_folgas_mecanicas_input
      )
      if grau > 0:
          print(f"   - {termo}: {grau:.2%}")

  print("→ Temperatura Ambiente:")
  for termo in temperatura_ambiente.terms:
      grau = fuzz.interp_membership(
          temperatura_ambiente.universe,
          temperatura_ambiente[termo].mf,
          temperatura_ambiente_input
      )
      if grau > 0:
          print(f"   - {termo}: {grau:.2%}")

  print("→ Tempo de Operação Contínua:")
  for termo in tempo_operacao_continua.terms:
      grau = fuzz.interp_membership(
          tempo_operacao_continua.universe,
          tempo_operacao_continua[termo].mf,
          tempo_operacao_continua_input
      )
      if grau > 0:
          print(f"   - {termo}: {grau:.2%}")

  # Inserir valores no sistema fuzzy
  simulador.input['resistencia_isolamento_eletrico'] = resistencia_isolamento_eletrico_input
  simulador.input['tensao_alimentacao'] = tensao_alimentacao_input
  simulador.input['presenca_folgas_mecanicas'] = presenca_folgas_mecanicas_input
  simulador.input['temperatura_ambiente'] = temperatura_ambiente_input
  simulador.input['tempo_operacao_continua'] = tempo_operacao_continua_input

  # Computar o resultado
  simulador.compute()

  # Saída
  if 'risco_falha' in simulador.output:
    resultado = simulador.output['risco_falha']
    print(f"\nResultado fuzzy: Risco de Falha = {resultado:.2f}")
  else:
    print("\nNenhuma regra foi ativada suficientemente com esses valores de entrada.")
  # Exibição gráfica dos conjuntos fuzzy
  print("\nExibindo gráficos...")
  risco_falha.view(sim=simulador)
  plt.show()

regras_ativas_motor()