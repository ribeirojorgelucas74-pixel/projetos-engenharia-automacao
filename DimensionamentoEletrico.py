def dimensionar_circuito(potencia, tensao):
    print(f"--- Dimensionando: {potencia}W em {tensao}V ---")

    corrente_projeto = potencia / tensao
    print(f"Corrente calculada: {corrente_projeto:.2f}A")

    tabela_cabos = {
        1.5: 17.5,
        2.5: 24.0,
        4.0: 32.0,
        6.0: 41.0,
        10.0: 57.0,
        16.0: 76.0
    }

    disjuntores_comerciais = [10, 16, 20, 25, 35, 40, 50, 63, 70, 80]

    bitola_escolhida = None
    capacidade_cabo = 0

    for bitola, capacidade in tabela_cabos.items():
        if capacidade >= corrente_projeto:
            bitola_escolhida = bitola
            capacidade_cabo = capacidade
            break

    if not bitola_escolhida:
        print("Erro: Corrente acima da capacidade suportada por este script")
        return

    disjuntor_escolhido = None
    for dj in disjuntores_comerciais:
        if dj >= corrente_projeto and dj <= capacidade_cabo:
            disjuntor_escolhido = dj
            break

    if not disjuntor_escolhido:
        for dj in disjuntores_comerciais:
            if dj <= capacidade_cabo:
                disjuntor_escolhido = dj

    print(f"-> Cabo Recomendado: {bitola_escolhida} mm² (Suporta até {capacidade_cabo}A)")
    print(f"-> Disjuntor Recomendado: {disjuntor_escolhido} A")

    if disjuntor_escolhido and disjuntor_escolhido < corrente_projeto:
        print("AVISO DE SEGURANÇA: Risco de desarmar constantemente na potência máxima!")

dimensionar_circuito(7500, 220)
