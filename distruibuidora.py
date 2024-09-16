# Dicionário com os valores de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentual(faturamento_estados):
    """Calcula o percentual de cada estado no faturamento total."""
    faturamento_total = sum(faturamento_estados.values())
    
    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        percentuais[estado] = percentual
    
    return faturamento_total, percentuais

def main():
    faturamento_total, percentuais = calcular_percentual(faturamento_estados)
    
    print(f"Faturamento total: R${faturamento_total:.2f}\n")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}% do faturamento total")

    input("\nPressione qualquer tecla para sair...")

if __name__ == "__main__":
    main()
