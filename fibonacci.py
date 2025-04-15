def pertence_a_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == b or n == 0

try:
    numero = int(input("Informe um número para verificar se está na sequência de Fibonacci: "))

    if pertence_a_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
