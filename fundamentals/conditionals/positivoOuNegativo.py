num = int(input("Digite um número inteiro: "))

sinal = (
    f"O número {num} é positivo"
    if num > 0
    else f"O número {num} é negativo"
    if num < 0
    else "Esse número é zero."
)

print(sinal)
