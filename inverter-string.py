def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

entrada = input("Digite uma string para inverter: ")

resultado = inverter_string(entrada)

print("String invertida:", resultado)
