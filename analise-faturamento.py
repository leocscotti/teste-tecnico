import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

faturamentos_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor = min(faturamentos_validos)
maior = max(faturamentos_validos)
media = sum(faturamentos_validos) / len(faturamentos_validos)

dias_acima_da_media = sum(1 for dia in faturamentos_validos if dia > media)

print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
