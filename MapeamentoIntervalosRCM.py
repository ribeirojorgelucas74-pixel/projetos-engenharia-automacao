intervalos = {
    "T1": "Preventiva (Baseada em tempo/cronograma)",
    "T2": "Preditiva (Monitoramento de condição/ Falha Potencial)",
    "T3": "Corretiva (Atuação na falha funcional/ quebra)"
}

ordem_solicitada = ["Corretiva", "Preventiva", "Preditiva"]
resultado = []

for tipo in ordem_solicitada:
    for t, desc in intervalos.items():
        if tipo in desc:
            resultado.append(t)
            break 

print(f"Ordem correspondente: {', '.join(resultado)}")
