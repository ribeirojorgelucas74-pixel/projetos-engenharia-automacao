def calcular_tensao_saida(ve, rf, r1):
    """Calcula a tensão de saída Vs de um amplificador não inversor."""
    ganho = 1 + (rf / r1)
    vs = ve * ganho
    return vs 

# Dados do Circuito
ve = 3.0        # Tensão de entrada (Volts)
rf = 2200.00    # Resistor de realimentação (Ohms)
r1 = 100.0      # Resistor R1 (Ohms)

resultado_vs = calcular_tensao_saida(ve, rf, r1)

print("======================================")
print(" SIMULAÇÃO - AMPLIFICADOR NÃO INVERSOR ")
print("======================================")
print(f"Tensão de Entrada (Ve): {ve:.2f} V")
print(f"Resistor Rf: {rf:.0f} Ohms")
print(f"Resistor R1: {r1:.0f} Ohms")
print("----------------------------------------")
print(f"Tensão de Saída (Vs): {resultado_vs:.2f} V")
print("======================================")
