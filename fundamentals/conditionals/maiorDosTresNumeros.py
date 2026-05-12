num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número:  "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    maior = num1
    print(f"O maior número dos três é {maior}")
elif num2 > num1 and num2 > num3:
    maior = num2
    print(f"O maior número dos três é {maior}")
else:
    maior = num3
    print(f"O maior número dos três é {maior}")
